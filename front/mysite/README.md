# mysite

화면 서버의 Django 프로젝트 설정 패키지입니다. `front/manage.py`가 `mysite.settings`를 사용합니다.

| 파일 | 역할 |
| --- | --- |
| `settings.py` | 템플릿 경로 `front/templates`, 정적 파일 `front/static`, 언어 `ko-kr`, 시간대 `Asia/Seoul` |
| `urls.py` | `strawberry` URL을 `/`와 `/strawberry/`에 연결, `/admin/` |
| `wsgi.py` | WSGI 진입점 |
| `asgi.py` | ASGI 진입점 |

데이터베이스 설정은 SQLite(`front/db.sqlite3`)가 켜져 있습니다. MariaDB 설정은 `settings.py`에 주석으로 남아 있습니다. 진단 결과의 영구 저장은 백엔드 MariaDB가 담당하고, 화면의 이력 목록은 브라우저 `localStorage`를 사용합니다.

`SECRET_KEY`는 `front/.env`에서 읽습니다. `DEBUG`는 현재 `True`입니다.

`ALLOWED_HOSTS`: `127.0.0.1`, `localhost`, `192.168.0.56`.
