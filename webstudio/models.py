from django.conf import settings
from django.db import models
from django.utils import timezone

class Works(models.Model):
    pass

class Order(models.Model):
    pass

class Employee(models.Model):
    employee_photo=models.ImageField(null=True)
    employee_fullname=models.CharField(max_length=300,default='')
    employee_specialization=models.CharField(max_length=300,default='')
    employee_email=models.EmailField(max_length=300,default='example@mail.com')
    employee_info=models.TextField(null=True)
    
    def __str__(self):
        return self.employee_fullname
# Create your models here.
