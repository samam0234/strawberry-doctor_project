# back

딸기 잎 진단 API 서버입니다. Django 6과 Django REST framework로 동작하고, 포트는 **8001**입니다.

## 하는 일

1. `POST /api/predict/`로 잎 이미지를 받습니다.
2. [`diagnosis/services/inference.py`](diagnosis/services/inference.py)가 EfficientNet-B3로 다섯 클래스를 분류하고 Grad-CAM 이미지를 만듭니다.
3. 원본, 결과, 신뢰도, Grad-CAM 경로를 MariaDB `DiagnosisResult`에 저장합니다.
4. `GET /api/history/`로 저장된 진단 목록을 돌려줍니다.

## 디렉터리

| 경로 | 설명 |
| --- | --- |
| [`config`](config/README.md) | 설정, URL, WSGI/ASGI |
| [`diagnosis`](diagnosis/README.md) | 진단 앱 |
| `manage.py` | Django 명령 진입점. 설정 모듈은 `config.settings` |
| `Dockerfile` | Python 3.12 이미지. `runserver 0.0.0.0:8001` |
| `requirements.txt` | Django, DRF, CORS, MySQL 드라이버, torch, torchvision, grad-cam, OpenCV |

업로드 파일은 `media/uploads/`, Grad-CAM은 `media/gradcam/`에 저장됩니다. `media/`는 git에서 제외합니다.

## 환경 변수 (`back/.env`)

`SECRET_KEY`, `DEBUG`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `ML_MODEL_PATH`

DB 기본 호스트는 `127.0.0.1`, 포트는 `3307`입니다. Compose 안에서는 DB 서비스 이름에 맞게 `DB_HOST`를 바꿉니다.

## 로컬 실행

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
```

Compose로 띄울 때는 저장소 루트에서 `docker compose up --build`를 실행합니다.
