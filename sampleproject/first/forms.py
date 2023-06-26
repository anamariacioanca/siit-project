from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name != name.title():
            raise ValidationError("The ame must begin with a capital letter")
        return name
    
    def clean(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        if name not in email:
            raise ValidationError("Name must appear in email")
        return self.cleaned_data
                                 
                        