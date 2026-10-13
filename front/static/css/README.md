# static/css

`bootstrap.min.css` 한 파일이 있습니다. 파일 이름은 Bootstrap이지만 내용은 **Font Awesome Free 6.5.0** 스타일시트입니다.

`templates/base.html`이 `{% static 'css/bootstrap.min.css' %}`로 이 파일을 불러옵니다. 아이콘 글리프는 별도 웹폰트(`static/webfonts/`)가 필요합니다. 웹폰트 디렉터리는 `.gitignore`에 있어 저장소에 포함되지 않습니다.
