from django.db import models


class Question(models.Model):
    """
    Model for PDPs to submit their questions.
    """
    title = models.TextField()
    body = models.TextField()
    votes = models.IntegerField()
    isFiltered = models.BooleanField()

    def __str__(self):
        return "Title={}\nVotes={}\nisFiltered={}"\
               .format(self.title, self.votes, self.isFiltered)
