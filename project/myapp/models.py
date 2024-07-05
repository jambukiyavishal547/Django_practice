from django.db import models
import datetime
from datetime import date
from django.utils import timezone
from django.http import Http404
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
        )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:   
        return self.choice_text

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
    
class Entry(models.Model):
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.headline