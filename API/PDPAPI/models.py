from django.db import models

# Create your models here.

#for PDPs to submit their questions
class Question(models.Model):
    question_text = models.CharField(max_length=200)