# strawberry

화면 페이지를 렌더링하는 Django 앱입니다. 질병 판별 계산은 하지 않고, 템플릿만 반환합니다.

| 파일 | 역할 |
| --- | --- |
| `urls.py` | 페이지 경로 |
| `views.py` | 각 경로의 `render` |
| `models.py` | 모델 없음 |
| `admin.py` | 관리자 등록 없음 |
| `apps.py` | `StrawberryConfig` |
| `tests.py` | 테스트 자리 |
| [`migrations`](migrations/README.md) | 앱 마이그레이션 패키지. 생성된 마이그레이션 없음 |
| [`services`](services/README.md) | 추론 코드를 두려고 만든 자리. 현재 비어 있음 |

## 경로

| 경로 | 뷰 | 템플릿 |
| --- | --- | --- |
| `/` | `home` | `templates/index.html` |
| `/training/` | `strawberry_training` | `templates/strawberry/training.html` |
| `/history/` | `strawberry_history` | `templates/strawberry/history.html` |
| `/myfarm/` | `strawberry_myfarm` | `templates/strawberry/myfarm.html` |
| `/report/` | `strawberry_report` | `templates/strawberry/report.html` |

같은 경로가 `/strawberry/` 아래에도 한 번 더 연결됩니다 (`mysite/urls.py`).

홈 뷰는 `static/image`의 Grad-CAM 샘플 경로를 템플릿에 넘깁니다. 진단 요청 자체는 `training.html`이 백엔드 `POST /api/predict/`로 보냅니다.
