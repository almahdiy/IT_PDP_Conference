from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core import serializers
import requests
from django.core import serializers
from django.shortcuts import render
from django.template import loader

from .models import Question, Authentication, MCQ, MCQOption, MAC, OptionVoting, QuestionVoting
from .serializers import QuestionSerializer, AuthenticationSerializer, MCQSerializer, MCQOptionSerializer, MACSerializer, OptionVotingSerializer, QuestionVotingSerializer



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




class QuestionVotingList(APIView):
    """
    List all Question objects, or add a new Question to the database.
    """
    def get(self, request, format=None):
        questions = QuestionVoting.objects.all()
        serializer = QuestionVotingSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionVotingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionVotingDetail(APIView):
    """
    Access a specific Question object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return QuestionVoting.objects.get(pk=pk)
        except QuestionVoting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionVotingSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionVotingSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class MACList(APIView):
    """
    List all Question objects, or add a new Question to the database.
    """
    def get(self, request, format=None):
        macs = MAC.objects.all()
        serializer = MACSerializer(macs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MACSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MACDetail(APIView):
    """
    Access a specific Question object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return MAC.objects.get(pk=pk)
        except MAC.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        MAC = self.get_object(pk)
        serializer = MACSerializer(MAC)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mac = self.get_object(pk)
        serializer = MACSerializer(mac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mac = self.get_object(pk)
        mac.delete()
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
            
        
class MCQList(APIView):
    """
    List all Question objects, or add a new Question to the database.
    """
    def get(self, request, format=None):
        MCQs = MCQ.objects.all()
        serializer = MCQSerializer(MCQs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MCQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MCQDetail(APIView):
    """
    Access a specific Question object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return MCQ.objects.get(pk=pk)
        except MCQ.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        MCQ = self.get_object(pk)
        serializer = MCQSerializer(MCQ)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        MCQ = self.get_object(pk)
        serializer = MCQSerializer(MCQ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        MCQ = self.get_object(pk)
        MCQ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class MCQOptionList(APIView):
    """
    List all option objects, or add a new option to the database.
    """
    def get(self, request, format=None):
        options = MCQOption.objects.all()
        serializer = MCQOptionSerializer(options, many=True)
        print("are we getting here?")
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MCQOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MCQOptionDetail(APIView):
    """
    Access a specific Question object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return MCQOption.objects.get(pk=pk)
        except MCQOption.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        MCQOption = self.get_object(pk)
        serializer = MCQOptionSerializer(MCQOption)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        MCQOption = self.get_object(pk)
        serializer = MCQOptionSerializer(MCQOption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        MCQOption = self.get_object(pk)
        MCQOption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def get_MCQ_options(request, pk):
    """
    Parameter: An MCQ's ID.
    Returns: The available options for that MCQ.
    """
    if(request.method == 'GET'):
        #SELECT option FROM McqOption WHERE MCQ_id=pk;
        q = MCQOption.objects.all().filter(MCQ_id=pk)
        return Response(MCQOptionSerializer(q, many=True).data)


@api_view(['POST'])
def vote(request):
    votes = [int(x) for x in dict(request.data)["votes"]]
    print("\n\n\n\nWE ARE VOTING ON QUESTIONS\n\n\n\n\n")
    for vote in votes:
        print("doing vote for question {}".format(vote))
        question = Question.objects.get(id=vote)
        try: #This person is trying to vote a thousand times. Don't let them!
            stored_votes = QuestionVoting.objects.get(unique=request.data["mac_address"], question_id=question.id)
            print("This question has been voted on before")
        except QuestionVoting.DoesNotExist:
            #create the OptionVoting for this combination so the user cannot vote next time
            print("This question has not been voted on before")
            dic = {"question_id" : question.id, "unique" : request.data["mac_address"]}
            serializer = QuestionVotingSerializer(data=dic)
            if serializer.is_valid():
                serializer.save()
            print("Vote has been created and user cannot vote on this same question next time")
            #The MAC address-option-question is valid; you can increment the count
            print("question.votes before: {}".format(question.votes))
            question.votes += 1
            print("question.votes after: {}".format(question.votes))

            serializer = QuestionSerializer(question, data={"body":question.body, "votes":question.votes, "isAppropriate":question.isAppropriate})
            if serializer.is_valid():
                serializer.save()
                print("Question with incerased vote has been saved.")
                # return Response(serializer.data)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(True)



    votes = [int(x) for x in dict(request.data)["votes"]]
    print(votes)
    for i in votes:
        question = Question.objects.get(pk=i)
        question.votes += 1
        serializer = QuestionSerializer(question, QuestionSerializer(question).data)
        if serializer.is_valid():
            serializer.save()

    return Response(True)


@api_view(['GET'])
def vote_count_ajax(request, pk):
    # echo in PHP.. I'm going to try returning concatinated string and see if that works...
    string = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>\n<response>"""
    #add vote count
    string += str(Question.objects.get(pk=pk).votes) + ""
    string += "</response>"
    print(string)
    # queryset = serializers.serialize('xml', Question.objects.all())
    return HttpResponse(string, content_type="application/xml")

@api_view(['GET'])
def question_count(request):
    print("Do we get here?")
    count = len(Question.objects.all())
    string = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>\n<response>"""
    #add vote count
    string += str(count)
    string += "</response>"
    return HttpResponse(string)




@api_view(['PUT'])
def option_vote(request, pk):
    option = MCQOption.objects.get(id=pk)
    #Check the mac address
    print(option.MCQ_id.id)
    #MAC address (how we're identifying the users: request.data["mac_address"]
  
    try: #This person is trying to vote a thousand times. Don't let them!
        stored_votes = OptionVoting.objects.get(unique=request.data["mac_address"], MCQ_id=option.MCQ_id.id)
    except OptionVoting.DoesNotExist:
        #create the OptionVoting for this combination so the user cannot vote next time
        dic = {"MCQ_id" : option.MCQ_id.id, "unique" : request.data["mac_address"]}
        serializer = OptionVotingSerializer(data=dic)
        if serializer.is_valid():
            serializer.save()
        #The MAC address-option-question is valid; you can increment the count
        print("\n\nGood up to here!\n\n")
        option.totalVotes += 1
        serializer = MCQOptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(False)

    
