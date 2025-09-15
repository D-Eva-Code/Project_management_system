from django.urls import path
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class Userform(UserCreationForm):
    class Meta:
        model= CustomUser
        fields=['name','email', 'password1', 'password2', 'role', 'matric_number', 'department','staff_id', 'supervisor',]
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'First-Middle-Last Name'})}

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


    def clean_email(self):
        email= self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This Email already Exits")
        return email
        
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

    def clean_name(self):
        name= self.cleaned_data['name']
        parts= name.split(' ',1)
        self.cleaned_data["first_name"]= parts[0]
        self.cleaned_data["last_name"]= parts[1] if len(parts)> 1 else ''
        return name

    def save(self, commit=True):
        user= super().save(commit=False)
        user.first_name=self.cleaned_data["first_name"]
        user.last_name=self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

        
class EmailAuthentication(AuthenticationForm):
    username= forms.EmailField(label="Email", 
    widget=forms.EmailInput(attrs={'autofocus':True, 'autocomplete':'off'}),
        )

    password= forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={'autocomplete':'off'}))

    # Override the form-level messages (no %(username)s interpolation)
    error_messages = {
        "invalid_login": _("Please enter a correct email and password. Note that both fields may be case-sensitive."),
        "inactive": _("This account is inactive."),}
    