from rest_framework import viewsets

from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer, SurveyUserAnswerSerializer
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer
# Create your views here.

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeSerializer

class SurveyUserAnswerViewSet(viewsets.ModelViewSet):
    queryset = SurveyUserAnswer.objects.all()
    serializer_class = SurveyUserAnswerSerializer