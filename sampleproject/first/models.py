from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"   
    
class CourseManager(models.Model):
    def final_year(self):
        return self.filter(year=5)    
    
class Course(models.Model):
    time = models.IntegerField(default=80)
    price =  models.FloatField(db_index=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True) 
    logo = models.FileField(null=True, blank=True)
    status = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    coordinator = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.CASCADE, related_name="coordinator") 
    year = models.IntegerField(default=1)

    objects = CourseManager()

    def __str__(self):
        return f"{self.name} {self.teacher}"
    
class Student(models.Model):
    class Meta:
        ordering = ["first_name", "last_name"]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)    
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"