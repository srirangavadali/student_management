from django.db import models

class Student(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    RollNumber=models.CharField(max_length=30)
    Class=models.CharField(max_length=30)
    Section=models.CharField(max_length=30)
    College=models.CharField(max_length=30)
