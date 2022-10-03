from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    search_fields=['name','description']

class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ("survey","survey_question_text")

    search_fields=['survey__name','survey_question_text']

class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ("survey","survey_question","survey_question_alternative_text")

    search_fields=['survey','survey_question','survey_question_alternative_text']

class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ("user","survey","survey_question","survey_question_alternative",)

    search_fields=["survey__name","survey_question__name","survey_question_alternative"]

admin.site.register(Survey,SurveyAdmin)
admin.site.register(SurveyQuestion,SurveyQuestionAdmin)
admin.site.register(SurveyQuestionAlternative,SurveyQuestionAlternativeAdmin)
admin.site.register(SurveyUserAnswer,SurveyAnswerAdmin)