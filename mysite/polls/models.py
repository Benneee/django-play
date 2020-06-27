import datetime
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # The use of ForeignKey here tells Django each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# With the information above, Django is able to create a database schema for this application
# It will also use the information to create a python database-access API for accessing Question and Choice objects

# This app needs to have been added to the project's apps first before the above happens