from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.db.models import Q


# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}!")

def courses(request):
    year = request.GET.get("year")
    all_courses = Course.objects.all().order_by("-year")
    if year is not None:   
        all_courses = all_courses.filter(Q(year__lte=int(year)) | Q(name__icontains="Course"))
    courses_name = [f"<a href='/course/{Course.id}'>{Course.name} year: {Course.year}</a>" for Course in all_courses]
    print(request.GET)
    return HttpResponse(f"{courses_name}")

def course(request, course_id):
    try:
        my_course = Course.objects.get(id=course_id)
        students = ["George"]
        students = my_course.student_set.all()
        return render(request, "course.html", {"my_course": my_course, "students": students})
    except Course.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
