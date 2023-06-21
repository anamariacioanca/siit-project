from django.db import models

# Create your models here.
class Course(models.Model):
    time = models.IntegerField(default=80)
    price =  models.FloatField()
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True) 

