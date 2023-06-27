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
        super().__init__(*args, **kwargs)    
        self.fields["courses"].queryset = Course.objects.filter(teacher__last_name="Popescu")


                                 
                        