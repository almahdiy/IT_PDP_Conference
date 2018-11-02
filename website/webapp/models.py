from django.db import models

# Create your models here.

#Used in the little login form
class Authentication(models.Model):
	sessionID = models.CharField(max_length=250)


#Used in the Q&A page - New question form
class Question(models.Model):
	body = models.CharField(max_length=1000)