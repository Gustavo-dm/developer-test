from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'surveys', views.SurveyViewSet)
# router.register(r'survey-question', views.SurveyQuestionViewSet)
# router.register(r'surveys-alternative', views.SurveyQuestionAlternativeViewSet)
# router.register(r'surveys-answers', views.SurveyUserAnswerViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('surveys_list/', views.survey_list),
    path('survey_question_list/', views.survey_question_list),
    path('survey_alternative_list/', views.survey_alternative_list),
    path('surveys_answer_list/', views.survey_answer_list),
    

] 