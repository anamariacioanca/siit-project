from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}!")

def courses(request):
    all_courses = Course.objects.all() # select * from courses;
    courses_name = [f"<a href='/course/{Course.id}'>{Course.name}</a>" for Course in all_courses]
    return HttpResponse(f"{courses_name}")

def course(request, course_id):
    try:
        my_course = Course.objects.get(id=course_id)
        return render(request, "course.html", {"my_course": my_course})
    except Course.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
