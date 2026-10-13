# config

백엔드 Django 프로젝트 설정 패키지입니다. `manage.py`와 `Dockerfile`이 이 패키지를 설정 모듈로 사용합니다.

| 파일 | 역할 |
| --- | --- |
| `settings.py` | MariaDB 연결, CORS, 미디어 경로, `ML_MODEL_PATH`, 언어 `ko-kr`, 시간대 `Asia/Seoul` |
| `urls.py` | `/admin/`, 진단 URL을 루트와 `/api/` 양쪽에 연결, 개발용 미디어 서빙 |
| `wsgi.py` | WSGI 진입점 (`config.settings`) |
| `asgi.py` | ASGI 진입점 (`config.settings`) |

설치된 앱은 Django 기본 앱과 `rest_framework`, `corsheaders`, `diagnosis`입니다.

`CORS_ALLOWED_ORIGINS`에는 화면 서버 `localhost:8000`, `127.0.0.1:8000`, Live Server `localhost:5500`, 발표용 `192.168.0.56:8000`이 들어 있습니다. 새 주소에서 화면을 열면 여기를 추가합니다.

비밀 키와 DB 비밀번호는 `settings.py`에 적지 않고 `back/.env`에서 읽습니다.
