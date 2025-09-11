from django.urls import path
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userform(UserCreationForm):
    # Email= forms.EmailField()
    # Name= forms.CharField(max_length=100)
    class Meta:
        model= User
        fields=['username','email', 'password1', 'password2', 'role', 'matricnumber', 'department','staff_id', 'supervisor']

    def clean(self):
        cleaned_data= super().clean()
        role= cleaned_data.get('role')

        if role== "student" and not cleaned_data.get("matric_number"):
            self.add_error("matric number", "Student must enter matric number")

        if role== "student" and not cleanded_data.get("supervisor"):
            self.add_error("matric number", "Student must select a supervisor")

        if role== "superisor" and not cleaned_data.get("staff_id"):
            self.add_error("staff_id", "Supervisor must enter staff ID")

        

        return cleaned_data