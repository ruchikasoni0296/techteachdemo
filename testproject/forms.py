from django import forms
from testproject.models import Student


class RegisterstForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname','lastname','email','username','gender']
        
        
        
