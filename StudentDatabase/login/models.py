from audioop import maxpp
from django.db import models

# Create your models here.

class student_details(models.Model):
    name = models.CharField(max_length=50)
    ad_no = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.name



