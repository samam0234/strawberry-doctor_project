# static

화면 서버가 그대로 내려주는 정적 파일입니다. `mysite/settings.py`의 `STATICFILES_DIRS`가 이 디렉터리를 가리키고, URL 접두사는 `/static/`입니다.

| 경로 | 내용 |
| --- | --- |
| [`css`](css/README.md) | 아이콘 스타일시트 |
| [`image`](image/README.md) | 홈과 안내에 쓰는 Grad-CAM 샘플 |

`base.html`은 여기에 더해 `/static/webfonts/css/all.min.css`를 불러옵니다. `webfonts/`는 `.gitignore` 대상이라 이 저장소에는 폰트 파일이 없습니다. 아이콘이 보이지 않으면 Font Awesome 6.5.0 웹폰트를 `front/static/webfonts/`에 두어야 합니다.

배포용으로 모으는 경로는 `staticfiles/`이며, 그 디렉터리도 git에서 제외합니다.
