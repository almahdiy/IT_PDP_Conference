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
    One-to-many relationship with MAC
    """
    question = models.TextField(default='')
    open_for_voting = models.BooleanField(default=True)


class MAC(models.Model):
    #Foreign keys represent many-to-one relationships
    #having a MAC address associated with an MCQ means that the user of that device
    #has already submitted a vote for this question, so they cannot vote multiple times
    # MCQs = models.ManyToManyField(MCQ, null=True)
    mac_address = models.IntegerField(default=0)
    

class MCQOption(models.Model):
    #Foreign keys represent many-to-one relationships
    MCQ_id = models.ForeignKey('MCQ', on_delete=models.CASCADE, null=True,) # When the question is deleted, the option will also be deleted.
    option = models.TextField(default='')
    totalVotes = models.IntegerField(default=0)
    

#table to help validate the vote before 
class OptionVoting(models.Model):
    MCQ_id = models.ForeignKey('MCQ', on_delete=models.CASCADE, null=True,) # When the question is deleted, the option will also be deleted.
    #MCQOption_id = models.ForeignKey('MCQOption', on_delete=models.CASCADE, null=True,) # When the question is deleted, the option will also be deleted.
    unique = models.IntegerField(default=0) #MAC address, IP, ...etc



#table to help validate the vote before 
class QuestionVoting(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, null=True,) # When the question is deleted, the option will also be deleted.
    unique = models.CharField(default="0.0.0.0", max_length=15) #MAC address, IP, ...etc
