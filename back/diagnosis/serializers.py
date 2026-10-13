# back/diagnosis/serializers.py

from rest_framework import serializers
from .models import DiagnosisResult

class DiagnosisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisResult
        fields = ['id', 'created_at', 'result', 'confidence', 'image', 'gradcam_image']
        read_only_fields = ['id', 'created_at']
