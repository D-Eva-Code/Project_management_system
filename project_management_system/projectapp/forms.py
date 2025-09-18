from django import forms


class UploadForm(forms.Form):
    title= forms.CharField(max_length=40)
    file = forms.FileField(label='Select a file', help_text= 'max. 42 megabytes')
    description= forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder':'Describe project or changes made'}))
    
    



