# diagnosis

잎 이미지를 받아 질병을 판별하고 결과를 저장하는 Django 앱입니다.

| 파일 | 역할 |
| --- | --- |
| `models.py` | `DiagnosisResult`. 촬영 시각, 원본 이미지, 결과 코드, 신뢰도, Grad-CAM |
| `serializers.py` | 이력 API용 `DiagnosisResultSerializer` |
| `views.py` | `PredictView` (`POST`), `HistoryView` (`GET`). 프로세스 시작 시 모델을 한 번 로드 |
| `urls.py` | `predict/`, `history/` |
| `admin.py` | 관리자 등록은 아직 비어 있습니다 |
| `apps.py` | `DiagnosisConfig` |
| `tests.py` | 테스트 자리입니다 |
| [`services`](services/README.md) | 모델 로드, 추론, Grad-CAM |
| [`migrations`](migrations/README.md) | `DiagnosisResult` 테이블 생성 |

`config/urls.py`가 이 URL을 `/`와 `/api/`에 모두 붙입니다. 화면은 `/api/predict/`를 호출합니다.

예측 응답 필드: `id`, `result`, `result_ko`, `confidence`, `gradcam_image`, `probabilities`.

결과 코드는 `normal`, `phytophthora`, `wilt`, `tipburn`, `yellowing`입니다. 목록은 최신 진단이 먼저 오도록 `created_at` 내림차순입니다.
