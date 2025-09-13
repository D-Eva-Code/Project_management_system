from django.shortcuts import render, redirect
from .forms import Userform
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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
                print("Redirecting to supervisor dashboard...") 
                # return redirect('supervisor_dashboard.html')
                return redirect('project:supervisor_dashboard')
        else:
            print(form.errors)
    else:
        form= Userform()
    return render(request, "register.html", {"form": form})

class RoleBasedLoginView(LoginView):
    template_name = "login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)#super here refers to formview. which handles form validation, rerendering and submission

    def get_success_url(self):
        if self.request.user.role == "student":
            return reverse("project:student_dashboard")
        elif self.request.user.role == "supervisor":
            return reverse("project:supervisor_dashboard")
        return reverse("register") 

@login_required
def log_out(request):
    if request.method=="POST":
        logout(request)
        messages.success(request, "Logged Out")
        return redirect('login')
        
  