from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userapp.models import CustomUser
from django.conf import settings
from .forms import UploadForm
from .models import Document
# Create your views here.
@login_required
def student(request):
    if request.user.is_authenticated:
        # author=CustomUser.objects.filter(owner=request.user)
        full_name=request.user.get_full_name
        if request.method=="POST":
            form= UploadForm(request.POST, request.FILES)
            if form.is_valid:
                new_form= Document(file= request.FILES['file'])
                new_form.save()
                messages.success(request, "File Successfully Uploaded")
        else:
            form= UploadForm()
        return render(request, 'student_dashboard.html',{"full_name":full_name, "form":form})
    


@login_required
def supervisor(request):
    # return HttpResponse("Home page")
    full_name= request.user.get_full_name if request.user.is_authenticated else ""
    return render(request, 'supervisor_dashboard.html', {"full_name":full_name})

@login_required
def projectupload(request):
    loop_form= Document.objects.all()

    return render(request, "project.html", {"loop_form":loop_form})