from django.urls import path
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class Userform(UserCreationForm):
    class Meta:
        model= CustomUser
        fields=['name','email', 'password1', 'password2', 'role', 'matric_number', 'department','staff_id', 'supervisor',]
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Enter Full name'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matric_number'].required= False
        self.fields['department'].required= False
        self.fields['staff_id'].required= False
        self.fields['supervisor'].required= False

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = (
                f"<div class='form-text text-light'>{self.fields[fieldname].help_text}</div>"
            )

    def clean(self):
        cleaned_data= super().clean()
        role= cleaned_data.get('role')

        
        if role=="student":
            required_fields= ["matric_number", "department", "supervisor"]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f"Student must enter {field.replace('_', ' ')}")  

        
        elif role== "supervisor":
            if not cleaned_data.get("staff_id"):
                self.add_error("staff_id", "Supervisor must enter staff ID")
 
            forbidden_fields= ["matric_number", "department", "supervisor"]
            for field in forbidden_fields:
                if cleaned_data.get(field):
                    self.add_error(field, f"Supervisor cannot have {field.replace('_', ' ')}")

        return cleaned_data