# front

딸기 닥터 화면 서버입니다. Django 6 템플릿으로 동작하고, 포트는 **8000**입니다. 질병 판별은 하지 않고 [`back`](../back/README.md) API를 호출합니다.

## 디렉터리

| 경로 | 설명 |
| --- | --- |
| [`mysite`](mysite/README.md) | 설정, URL, WSGI/ASGI |
| [`strawberry`](strawberry/README.md) | 페이지 뷰와 URL |
| [`templates`](templates/README.md) | HTML |
| [`static`](static/README.md) | 아이콘 CSS, Grad-CAM 샘플 이미지 |
| [`docs`](docs/README.md) | 사용 안내와 작업 메모, 화면 캡처 |
| `manage.py` | 설정 모듈 `mysite.settings` |
| `Dockerfile` | Python 3.12. `runserver 0.0.0.0:8000` |
| `requirements.txt` | Django 6.0.4, django-environ, python-dotenv, requests |

## 페이지

| 주소 | 화면 |
| --- | --- |
| `/` | 랜딩 |
| `/training/` | 사진 업로드, 영역 자르기, 진단 |
| `/history/` | 브라우저에 저장된 진단 이력 |
| `/myfarm/` | 정상 비율로 계산하는 농장 건강 점수 |
| `/report/` | 연구 보고서 |

진단 이력 목록은 `localStorage`에 있습니다. MariaDB 저장은 백엔드 `DiagnosisResult`가 담당합니다.

## 실행

`front/.env`에 `SECRET_KEY`를 넣습니다. DB를 이 서버에 붙일 때는 `settings.py`의 MariaDB 주석과 `.env`의 `ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`를 함께 맞춥니다. 기본 설정은 SQLite입니다.

```bash
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

Compose로 띄울 때는 저장소 루트에서 `docker compose up --build`를 실행합니다. 화면은 백엔드가 뜬 뒤에 열립니다.

`training.html`은 API를 `http://192.168.0.56:8001`로 호출합니다. 로컬에서 주소가 다르면 그 파일을 수정합니다.
