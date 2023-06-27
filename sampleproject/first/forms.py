from django import forms
from django.core.exceptions import ValidationError
from .models import Teacher, Student, Course

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 1, "cols": 20}))

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name != name.title():
            raise ValidationError("The ame must begin with a capital letter")
        return name
    
    def clean(self):
        name = self.cleaned_data.get["name", ""]
        email = self.cleaned_data.get["email", ""]
        if name not in email:
            raise ValidationError("Name must appear in email")
        return self.cleaned_data
    
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"    

    #phone_number = forms.CharField(widget=forms.PasswordInput)
    #active = forms.BooleanField()   
    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []

    def __init__(self, *args, **kwargs):
        last_name_teacher = kwargs.pop("filter_teacher")
        super().__init__(*args, **kwargs)  
        if last_name_teacher is not None:
            course_qs = Course.objects.filter(teacher__last_name=last_name_teacher) 
        else:
            course_qs = Course.objects.all()    
        self.fields["courses"].queryset = course_qs

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)



                                 
                        