from django.shortcuts import render
from .forms import userform
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
        form= userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new user successfully created")
            if role== "student":
                return redirect('project:student_dashboard')
            else:    
                return redirect('project:supervisor_dashboard')

    else:
        form= userform()
    return render(request, "register.html", {"form": form, "messages":messages})

