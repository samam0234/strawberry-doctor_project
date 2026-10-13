# templates/strawberry

진단 이후 화면입니다. 모두 `templates/base.html`을 상속합니다.

| 파일 | 경로 | 하는 일 |
| --- | --- | --- |
| `training.html` | `/training/` | 잎 사진을 올리고 Cropper.js로 영역을 자른 뒤 `POST /api/predict/`로 보냅니다. 신뢰도 85% 이상이면 병명, 클래스별 확률 차트, Grad-CAM을 보여주고 `localStorage`에 이력을 남깁니다. 70% 이상 85% 미만은 불확실, 그 미만은 오류 화면입니다. |
| `history.html` | `/history/` | `localStorage`의 진단 이력을 검색, 필터, 상세 모달로 보여 줍니다. |
| `myfarm.html` | `/myfarm/` | 농장 건강 점수를 계산합니다. 점수 = (정상 진단 수 / 전체 진단 수) × 100. |
| `report.html` | `/report/` | 데이터셋과 EfficientNet 기준 모델을 설명하는 연구 보고서 화면입니다. |

`training.html`의 API 주소는 `http://192.168.0.56:8001`로 고정되어 있습니다. 백엔드를 다른 호스트에서 띄우면 이 파일을 수정합니다.

서버에 남는 진단 이력 API는 `GET /api/history/`입니다. 이 페이지들의 목록은 그 API가 아니라 브라우저 저장소를 읽습니다.
