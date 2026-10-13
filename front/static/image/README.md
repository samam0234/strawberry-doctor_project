# static/image

홈 화면과 안내에 쓰는 딸기 잎 Grad-CAM 샘플입니다. 사용자가 업로드한 진단 사진이 아닙니다. 업로드 파일은 백엔드 `media/`에 저장됩니다.

| 파일 | 사용처 |
| --- | --- |
| `strawberry_gradCam_image.PNG` | 홈 대표 이미지 (`views.home`의 `gradcam_image`) |
| `gradcam1.jpg` … `gradcam6.jpg` | 홈에 넘기는 샘플 (`gradcam1` … `gradcam6`) |

경로는 `strawberry/views.py`의 `home`이 `static` 템플릿 태그로 만듭니다.
