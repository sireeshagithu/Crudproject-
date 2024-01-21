from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=34)
    mail = models.EmailField(max_length=35)
    age = models.IntegerField()