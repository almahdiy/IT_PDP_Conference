from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Question, Authentication
from .serializers import QuestionSerializer, AuthenticationSerializer



SESSION_ID = "1234"

class QuestionList(APIView):
    """
    List all Question objects, or add a new Question to the database.
    """
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    Access a specific Question object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', ])
def authenticate(request):
    """
    Takes a session ID and compares it to a constant value
    """
    print("HERE")
    if(request.method == 'POST'):
        #data is a dictionary that has the username and the password the user tried
        data = AuthenticationSerializer(request.data).data
        submission = data["sessionID"]
        if(submission == SESSION_ID):
            return Response(True)
        else:
            return Response(False)
            
        