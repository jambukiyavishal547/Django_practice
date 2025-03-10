from django.db import models

# Create your models here.

class Teacher(models.Model):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    
class Student(models.Model):

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname