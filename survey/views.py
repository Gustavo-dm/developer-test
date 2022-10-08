from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer, SurveyUserAnswerSerializer
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer
# Create your views here.

# class SurveyViewSet(viewsets.ModelViewSet):
#     queryset = Survey.objects.all()
#     serializer_class = SurveySerializer

# class SurveyQuestionViewSet(viewsets.ModelViewSet):
#     queryset = SurveyQuestion.objects.all()
#     serializer_class = SurveyQuestionSerializer

# class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
#     queryset = SurveyQuestionAlternative.objects.all()
#     serializer_class = SurveyQuestionAlternativeSerializer

# class SurveyUserAnswerViewSet(viewsets.ModelViewSet):
#     queryset = SurveyUserAnswer.objects.all()
#     serializer_class = SurveyUserAnswerSerializer   

@csrf_exempt
def survey_list(request):
    if request.method == 'GET':
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return JsonResponse(serializer.data, safe=False)
 
 
def survey_question_list(request):

    if request.method == 'GET':
        surveys_answer = SurveyQuestion.objects.all()
        serializer = SurveyQuestionSerializer(surveys_answer, many=True)
        return JsonResponse(serializer.data, safe=False)

def survey_alternative_list(request):

    if request.method == 'GET':
        surveys_answer = SurveyQuestionAlternative.objects.all()
        serializer = SurveyQuestionAlternativeSerializer(surveys_answer, many=True)
        return JsonResponse(serializer.data, safe=False)

def survey_answer_list(request):

    if request.method == 'GET':
        surveys_answer = SurveyUserAnswer.objects.all()
        serializer = SurveyUserAnswerSerializer(surveys_answer, many=True)
        return JsonResponse(serializer.data, safe=False)

