# templates

화면 HTML입니다. `mysite/settings.py`가 이 디렉터리를 템플릿 경로로 등록합니다.

| 파일 | 페이지 |
| --- | --- |
| `base.html` | 공통 레이아웃. 상단 메뉴(진단하기, 진단 이력, 내 농장, 연구 보고서), Tailwind CDN, Font Awesome |
| `index.html` | `/` 랜딩. 진단 시작 안내와 Grad-CAM 샘플 |
| [`strawberry`](strawberry/README.md) | 진단, 이력, 내 농장, 연구 보고서 |

페이지 템플릿은 `base.html`을 상속합니다. 진단 API 호출과 이력 저장 스크립트는 각 페이지 안에 있습니다.
