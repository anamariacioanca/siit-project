from django.contrib import admin

# Register your models here.
from .models import Course, Teacher

admin.site.register(Course)
admin.site.register(Teacher)