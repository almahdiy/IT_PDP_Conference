from django.db import models


class Question(models.Model):
    """
    Model for PDPs to submit their questions.
    """
    body = models.TextField(default='')
    votes = models.IntegerField(default=0)
    isAppropriate = models.BooleanField(default=False)

    def __str__(self):
        return self.body
