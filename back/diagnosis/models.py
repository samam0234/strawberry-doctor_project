from django.db import models

# Create your models here.

class DiagnosisResult(models.Model):
    # 진단 일시 — 저장 시점 자동 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # 업로드된 원본 딸기 잎 이미지
    image = models.ImageField(upload_to='uploads/')

    # 진단 결과: 5개 클래스 중 하나
    DISEASE_CHOICES = [
        ('normal',    '정상'),
        ('phytophthora', '역병'),
        ('wilt',      '시들음병'),
        ('tipburn',   '잎끝마름'),
        ('yellowing', '황화'),
    ]
    result = models.CharField(max_length=20, choices=DISEASE_CHOICES)

    # 신뢰도 (예: 94.7)
    confidence = models.FloatField()

    # Grad-CAM 히트맵 이미지 (나중에 채워지므로 null 허용)
    gradcam_image = models.ImageField(upload_to='gradcam/', null=True, blank=True)

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.get_result_display()} ({self.confidence:.1f}%)"

    class Meta:
        ordering = ['-created_at']  # 최신 진단이 먼저 오도록