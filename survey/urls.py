from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'surveys', views.SurveyViewSet)
router.register(r'survey-question', views.SurveyQuestionViewSet)
router.register(r'surveys-alternative', views.SurveyQuestionAlternativeViewSet)
router.register(r'surveys-answers', views.SurveyUserAnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 