from rest_framework import serializers
from .models import Question, Authentication, MCQ, MCQOption, MAC, OptionVoting, QuestionVoting


#For the QA session
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'      # Do this to return everything


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = '__all__'    


class MCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQ
        fields = '__all__'    


class MCQOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQOption
        fields = '__all__'    


class MACSerializer(serializers.ModelSerializer):
    class Meta:
        model = MAC
        fields = '__all__'    


class OptionVotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionVoting
        fields = '__all__'    


class QuestionVotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVoting
        fields = '__all__'    

