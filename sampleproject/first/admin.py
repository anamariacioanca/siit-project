from django.contrib import admin

# Register your models here.
from .models import Course, Teacher, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "teacher","status")
    list_select_related = ("teacher", )
    list_filter = ("teacher", "status", "year")
    search_fields = ("name", "teacher__last_name")

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)
admin.site.register(Student)