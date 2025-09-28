from django import forms
from .models import Document

class UploadForm(forms.ModelForm):
    
    # file = forms.FileField(label='Select a file', help_text= 'max. 42 megabytes')
    # description= forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder':'Describe project or changes made'}))
    class Meta:
        model= Document
        fields=['file','title', 'description']
        widgets={
            'description': forms.Textarea(attrs={'placeholder':'Describe project or changes made'})
        }
        label={
            'file': 'Select a file'
        }
        help_text={
            'file': 'max. 42 megabytes'
        }

    
    



