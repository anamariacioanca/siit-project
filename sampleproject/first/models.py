from django.db import models

# Create your models here.
class Course(models.Model):
    time = models.IntegerField(default=80)
    price =  models.FloatField(db_index=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True) 
    logo = models.FileField(null=True, blank=True)
    status = models.BooleanField(default=True)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)