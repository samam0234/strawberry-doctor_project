from django.urls import path
# . 은 현재 폴더를 의미한다. board/views.py 파일을 가져와라 라는 의미
from . import views

urlpatterns = [
    path('', views.home, name='home'),    # 홈페이지
    path('training/', views.strawberry_training, name='strawberry_training'),    # 이미지 학습 페이지
    path('history/', views.strawberry_history, name='strawberry_history'),    # 이미지 학습 데이터 저장 페이지
    path('myfarm/', views.strawberry_myfarm, name='strawberry_myfarm'),    # 내 농장 데이터 페이지
    path('report/', views.strawberry_report, name='strawberry_report'),    # 리포트(여담 및 관련 학습 모델 설명) 데이터 페이지
]

# 특별한 상황으로 인해 수정 허락을 받지 않는 이상 아니면 함부로 건들지 마시오.