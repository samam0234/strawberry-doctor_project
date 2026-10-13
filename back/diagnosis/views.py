from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.conf import settings
from .models import DiagnosisResult
from .serializers import DiagnosisResultSerializer
from diagnosis.services.inference import predict, load_model

# 서버 시작 시 모델 1회 로드
load_model(settings.ML_MODEL_PATH)


class PredictView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': '이미지 파일이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        prediction = predict(image)

        # ✅ 콘솔에서 확인용
        print("prediction 전체:", prediction)
        print("probabilities:", prediction.get('probabilities'))

        diagnosis = DiagnosisResult.objects.create(
            image=image,
            result=prediction['result'],
            confidence=prediction['confidence'],
            gradcam_image=prediction.get('gradcam_image'),
        )
        
        # ✅ 직접 딕셔너리로 응답 구성
        return Response({
            'id': diagnosis.id,
            'result': prediction['result'],
            'result_ko': prediction['result_ko'],
            'confidence': prediction['confidence'],
            'gradcam_image': '/media/' + str(diagnosis.gradcam_image),
            'probabilities': prediction['probabilities'],
        }, status=status.HTTP_201_CREATED)


class HistoryView(APIView):
    def get(self, request):
        results = DiagnosisResult.objects.all()
        serializer = DiagnosisResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    