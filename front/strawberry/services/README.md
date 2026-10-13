# strawberry/services

화면 앱 안에 두었던 추론 모듈 자리입니다.

| 파일 | 상태 |
| --- | --- |
| `inference.py` | 비어 있음 |
| `gradcam.py` | 비어 있음 |

모델 로드, 분류, Grad-CAM 저장은 [`back/diagnosis/services/inference.py`](../../../back/diagnosis/services/inference.py)에서 합니다. 이 두 파일을 채우기 전에는 화면이 백엔드 API를 호출하는 현재 흐름을 유지합니다.
