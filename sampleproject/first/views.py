from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Course, Student, Teacher
from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from .forms import ContactForm, LoginForm, TeacherForm, StudentForm


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
    return render(request, "base.html", {})

def profile(request):
    return render(request, "profile.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "Validated form"
        else:
            message = "Invalid form"    
    else:
        form = ContactForm()
        message = ""        
    context = {
        "form": form,
        "message": message
    }
    return render(request, "contact.html", context)

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = TeacherForm()
    context = {
        "form": form
    }
    return render(request, "add_teacher.html", context)

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(data=request.POST, instance=teacher)
        if form.is_valid():
            form.save()
    else:    
        form = TeacherForm(instance=teacher)
    context = {
        "form": form
    }
    return render(request, "edit_teacher.html", context)

def add_student(request):
    teacher = request.GET.get("teacher")
    if request.method == "POST":
        form = StudentForm(request.POST, filter_teacher=teacher)
        if form.is_valid():
            student = form.save()
            return redirect(f"/students?student_id={student.id}")    
    else:    
        form = StudentForm(filter_teacher=teacher)
    context = {
        "form": form
    }
    return render(request, "add_student.html", context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()    
    context = {
        "form": LoginForm()
    }
    return render(request, "login.html", context)
