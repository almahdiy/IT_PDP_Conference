from django.db import models



#For the Q&A session; PDPs are going to be able to submit questions and vote on already submitted questions
class Question(models.Model):
    """
    Model for PDPs to submit their questions.
    """
    body = models.TextField(default='')
    votes = models.IntegerField(default=0)
    isAppropriate = models.BooleanField(default=False)

    def __str__(self):
        return self.body




class Authentication(models.Model):
    """
    Authentication mechanism so that only PDPs present at the auditorium can access the website.
    """
    sessionID = models.CharField(max_length=250)


#Multiple choice questions for the Ice Breaker activity
class MCQ(models.Model):
    """
    Model for the Ice Breaker activity.
    One-to-many relationship with MCQOption
    """
    question = models.TextField(default='')



class MCQOption(models.Model):
    #Foreign keys represent many-to-one relationships
    MCQ_id = models.ForeignKey('MCQ', on_delete=models.CASCADE, null=True,) # When the question is deleted, the option will also be deleted.
    option = models.TextField(default='')
    totalVotes = models.IntegerField(default=0)