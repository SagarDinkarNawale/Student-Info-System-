from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30,default='')
    address = models.CharField(max_length=30,default='')
    mobile = models.CharField(max_length=30,default='')
    course = models.CharField(max_length=30,default='')
    city = models.CharField(max_length=30,default='')
    def __str__(self):
        return self.name



