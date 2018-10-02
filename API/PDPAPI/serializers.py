from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question        # What model you want to serializers
        fields = '__all__'      # Do this to return everything
