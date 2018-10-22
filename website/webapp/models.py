from django.db import models

# Create your models here.

#Used in the little login form
class Authentication(models.Model):
	sessionID = models.CharField(max_length=250)