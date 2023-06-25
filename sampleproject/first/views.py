from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Student
from django.db.models import Q, F


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
    all_courses = all_courses.only("name", "teacher")
    return render(request, "courses.html", {"courses": all_courses})

def course(request, course_id):
    try:
        my_course = Course.objects.get(id=course_id)
        students = ["George"]
        students = my_course.student_set.all()
        return render(request, "course.html", {"my_course": my_course, "students": students})
    except Course.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
    
def students(request):
    students = Student.objects.all().prefetch_related("courses")
    # for student in students:
    #     student.year = student.year + 1
    #     student.save()
    #students.update(year=F('year') + 1)
    return render(request, "students.html", {"students": students})   

def main(request):
    return render(request, "main.html", {})

def profile(request):
    return render(request, "profile.html", {})
