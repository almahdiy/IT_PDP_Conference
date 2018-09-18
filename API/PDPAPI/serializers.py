from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question #what model you want to serializers
        fields = '__all__' #do this to return everything