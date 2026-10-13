# back/diagnosis/services/inference.py

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io
from pytorch_grad_cam import GradCAM
import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
import uuid
import collections

# ── class_names.json의 class_to_idx 기준으로 맞춤 ──
IDX_TO_LABEL = {
    0: 'wilt',           # 시들음병
    1: 'phytophthora',   # 역병
    2: 'tipburn',        # 잎끝마름
    3: 'normal',         # 정상
    4: 'yellowing',      # 황화
}

# 화면 표시용 한글 매핑
LABEL_TO_KO = {
    'wilt':         '시들음병',
    'phytophthora': '역병',
    'tipburn':      '잎끝마름',
    'normal':       '정상',
    'yellowing':    '황화',
}

_model = None
_device = None
_input_size = 300  # model_config.json 기준 기본값


def build_model() -> nn.Module:
    """model_config.json 기준: efficientnet_b3, num_classes=5"""
    model = models.efficientnet_b3(weights=None)
    in_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.3, inplace=True),
        nn.Linear(in_features, 5),
    )
    return model


def load_model(model_path: str):
    global _model, _device, _input_size

    _device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    _model = build_model().to(_device)

    checkpoint = torch.load(model_path, map_location=_device, weights_only=False)


    if isinstance(checkpoint, (dict, collections.OrderedDict)) and ('model_state' in checkpoint or 'model_state_dict' in checkpoint):
        state_dict = checkpoint.get('model_state') or checkpoint.get('model_state_dict')
    else:
        # 가중치가 바로 저장된 경우 (OrderedDict)
        state_dict = checkpoint

    _model.load_state_dict(state_dict)
    _model.eval()

    # input_size 우선순위: ① .pth 안 키 → ② .env의 ML_INPUT_SIZE → ③ 기본값 300
    _input_size = (
        int(getattr(settings, 'ML_INPUT_SIZE', 0))
        or 300
    )

    print(f"[inference] 로드 완료 | 모델: EfficientNet-B3 | device: {_device} | input_size: {_input_size}")


def predict(image_file) -> dict:
    if _model is None:
        raise RuntimeError("모델이 로드되지 않았습니다. load_model()을 먼저 호출하세요.")

    image_bytes = image_file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

    transform = transforms.Compose([
        transforms.Resize((_input_size, _input_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    tensor = transform(image).unsqueeze(0).to(_device)

    # 추론
    with torch.no_grad():
        outputs = _model(tensor)
        probs = torch.softmax(outputs, dim=1)[0]
        pred_idx = probs.argmax().item()
        confidence = probs[pred_idx].item() * 100

    # Grad-CAM
    gradcam = GradCAM(model=_model, target_layers=[_model.features[-1]])
    cam = gradcam(tensor)
    cam_img = (cam[0] * 255).astype(np.uint8)
    cam_img = cv2.applyColorMap(cam_img, cv2.COLORMAP_JET)

    original = image.resize((_input_size, _input_size))
    original_np = np.array(original)
    original_bgr = cv2.cvtColor(original_np, cv2.COLOR_RGB2BGR)
    cam_resized = cv2.resize(cam_img, (_input_size, _input_size))
    blended = cv2.addWeighted(original_bgr, 1.0, cam_resized, 0.45, 0)

    gradcam_filename = f"gradcam_{uuid.uuid4().hex[:8]}.jpg"
    gradcam_path = f"gradcam/{gradcam_filename}"
    default_storage.save(gradcam_path, ContentFile(cv2.imencode('.jpg', blended)[1].tobytes()))

    label = IDX_TO_LABEL[pred_idx]

    return {
        'result': label,
        'result_ko': LABEL_TO_KO[label],
        'confidence': round(confidence, 1),
        'gradcam_image': gradcam_path,
        'probabilities': {   # ←←← 이 부분 추가
            'wilt':         round(probs[0].item() * 100, 1),  # 0: 시들음병
            'phytophthora': round(probs[1].item() * 100, 1),  # 1: 역병
            'tipburn':      round(probs[2].item() * 100, 1),  # 2: 잎끝마름
            'normal':       round(probs[3].item() * 100, 1),  # 3: 정상
            'yellowing':    round(probs[4].item() * 100, 1),  # 4: 황화
        }
    }
    