# 딸기 닥터 (Strawberry Doctor)

딸기 잎 사진으로 질병을 판별하는 웹 서비스입니다. 화면은 Django 템플릿(`front`)이 그리고, 진단 API는 Django REST(`back`)가 EfficientNet-B3와 Grad-CAM으로 처리합니다. 진단 기록은 MariaDB에 저장합니다.

## 서비스 구성

| 디렉터리 | 역할 | 기본 주소 |
| --- | --- | --- |
| [`front`](front/README.md) | 진단, 이력, 내 농장, 연구 보고서 화면 | http://localhost:8000 |
| [`back`](back/README.md) | 예측 API, Grad-CAM, 진단 결과 저장 | http://localhost:8001 |
| [`ml`](ml/README.md) | EfficientNet-B3 학습 가중치 | |
| MariaDB (`docker-compose.yml`) | 진단 결과 저장 | `localhost:3307` |

## 진단 클래스

| 코드 | 화면 이름 |
| --- | --- |
| `normal` | 정상 |
| `phytophthora` | 역병 |
| `wilt` | 시들음병 |
| `tipburn` | 잎끝마름 |
| `yellowing` | 황화 |

모델 출력 인덱스 순서는 [`back/diagnosis/services/inference.py`](back/diagnosis/services/inference.py)의 `IDX_TO_LABEL`을 따릅니다. `normal`은 3번입니다.

## 실행

Docker Compose는 루트 `.env`에서 DB 계정을 읽고, `back`과 `front` 컨테이너는 각자 디렉터리의 `.env`를 읽습니다. `.env`는 저장소에 포함하지 않습니다.

| 파일 | 키 |
| --- | --- |
| 루트 `.env` | `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` |
| `back/.env` | `SECRET_KEY`, `DEBUG`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `ML_MODEL_PATH` |
| `front/.env` | `SECRET_KEY`. DB 키도 둘 수 있으나 화면 서버는 현재 SQLite를 사용합니다. |

`ML_MODEL_PATH`는 [`ml`](ml/README.md)의 `.pth` 파일을 가리킵니다.

```bash
docker compose up --build
```

- 화면: http://localhost:8000
- 예측: `POST http://localhost:8001/api/predict/` (`image` 파일)
- 이력: `GET http://localhost:8001/api/history/`
- 관리자: http://localhost:8001/admin/

진단 페이지는 브라우저에서 `http://192.168.0.56:8001/api/predict/`로 요청합니다. API 주소가 달라지면 [`front/templates/strawberry/training.html`](front/templates/strawberry/training.html)의 주소를 맞춥니다. `back`의 `ALLOWED_HOSTS`와 `CORS_ALLOWED_ORIGINS`도 같은 호스트를 허용해야 합니다.

## 문서

화면 사용법과 이전 작업 메모는 [`front/docs`](front/docs/README.md)에 있습니다.
