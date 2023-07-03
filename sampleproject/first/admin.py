from django.contrib import admin

# Register your models here.
from .models import Course, Teacher, Student
from django.db.models import F
from .forms import StudentAdminForm

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "teacher","status")
    list_select_related = ("teacher", )
    list_filter = ("teacher", "status", "year")
    search_fields = ("name", "teacher__last_name")

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)

def year_pass(modeladmin, request, queryset):
    queryset.update(year=F('year')+1)
    # for student in queryset:
    #     student.year = student.year + 1
    #     student.save()
    return    

class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "year")
    list_per_page = 10
    #change_list_template = "add_student.html"
    actions = (year_pass, )
    fieldsets = [
        ("", {"fields": ["first_name", "last_name"]}),
        ("Contact", {"fields": ["email", "phone_number"], "classes": ("collapse", )}),
        ("Courses", {"fields": ["courses"]})
    ]
    form = StudentAdminForm
    


admin.site.register(Student, StudentAdmin)