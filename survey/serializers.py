from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('__all__')

class SurveyQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ('__all__')

class SurveyQuestionAlternativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = ('__all__')

class SurveyUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyUserAnswer
        fields = ('__all__')

