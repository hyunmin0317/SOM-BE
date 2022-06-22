from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from question.models import Question
from question.serializers import QuestionSerializer


class QuestionAPI(APIView):
    def get(self, request, category):
        question = Question.objects.filter(category=category)
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
