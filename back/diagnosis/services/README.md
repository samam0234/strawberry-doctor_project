# diagnosis/services

진단 모델 추론입니다. 화면 서버의 `front/strawberry/services`는 비어 있고, 실제 추론은 이 파일에서 합니다.

## inference.py

- 구조: EfficientNet-B3, 분류기 Dropout 0.3 + Linear(5). 가중치는 `ML_MODEL_PATH`의 `.pth`
- 입력 크기: 기본 300. 환경 변수로 덮어쓸 때는 `settings.ML_INPUT_SIZE`를 사용
- 전처리: RGB, ImageNet 평균/표준편차
- 장치: CUDA가 있으면 CUDA, 없으면 CPU
- Grad-CAM: 마지막 feature 레이어. 원본과 JET 히트맵을 섞어 `media/gradcam/`에 JPEG로 저장

클래스 인덱스는 학습 때의 `class_to_idx`와 같아야 합니다.

| 인덱스 | 코드 | 한글 |
| --- | --- | --- |
| 0 | `wilt` | 시들음병 |
| 1 | `phytophthora` | 역병 |
| 2 | `tipburn` | 잎끝마름 |
| 3 | `normal` | 정상 |
| 4 | `yellowing` | 황화 |

`views.py`가 서버 기동 시 `load_model()`을 호출합니다. 경로가 비어 있거나 파일이 없으면 서버가 뜨다가 추론 단계에서 실패합니다.
