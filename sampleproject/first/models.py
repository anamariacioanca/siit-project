from django.db import models

# Create your models here.
class Course(models.Model):
    time = models.IntegerField(default=80)
    price =  models.FloatField()
    description = models.TextField()
    name = models.CharField(max_length=30)