"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# back/config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect   # ← 이 줄 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    # ←←← root(메인 페이지)와 모든 일반 페이지를 diagnosis.urls로 연결
    path('', include('diagnosis.urls')),
    # API는 /api/ 하위로 유지 (기존 방식)
    path('api/', include('diagnosis.urls')),  # ← 이 줄 추가
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)