from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pubdate = models.DataTimeField('date published')

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=CASCADE)
  choice_text = models.CharField(_MAX_LENGTH=200)
  vote = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
    


