from django import forms
from .models import Document

class UploadForm(forms.ModelForm):
    title= forms.CharField(max_length=40)
    # file = forms.FileField(label='Select a file', help_text= 'max. 42 megabytes')
    description= forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder':'Describe project or changes made'}))
    class Meta:
        model= Document
        fields=['file']
        # widgets={
        #     'file': forms.FileField(attrs={'help_text':'max, 42 megabytes', 'label':'Select a file'})
        # }
        label={
            'file': 'Select a file'
        }
        help_text={
            'file': 'max. 42 megabytes'
        }

    
    



