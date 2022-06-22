from django.urls import path
from question.views import QuestionAPI


urlpatterns = [
    path('<str:category>/', QuestionAPI.as_view()),
]
