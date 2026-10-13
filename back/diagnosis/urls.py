# back/diagnosis/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.PredictView.as_view(), name='predict'),
    path('history/', views.HistoryView.as_view(), name='history'),
]