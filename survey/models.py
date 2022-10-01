from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

# Create your models here.
User= get_user_model()

class Survey(models.Model):
    name = models.CharField(max_length=256,default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question_text = models.CharField(max_length=256,default=None)

    def __str__(self):
        return self.survey_question_text

class SurveyQuestionAlternative(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE,default=None)
    survey_question_alternative_text = models.CharField(max_length=256,default=None)

    def __str__(self):
        return self.survey_question_alternative_text

class SurveyUserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE,default=None)
    survey_question_alternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE,default=None)



    def __str__(self):
        return f'{self.survey_question_alternative.survey_question_alternative_text}'