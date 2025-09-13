from django.shortcuts import render, redirect
from .forms import Userform
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
        form= Userform(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            print(role)
            form.save()
            messages.success(request, "new user successfully created")
            if role== "student":
                print("Redirecting to student dashboard...")
                # return redirect('student_dashboard.html')
                return redirect('project:student_dashboard')
            else:   
                print("Redirecting to student dashboard...") 
                # return redirect('supervisor_dashboard.html')
                return redirect('project:supervisor_dashboard')
        else:
            print(form.errors)
    else:
        form= Userform()
    return render(request, "register.html", {"form": form})

