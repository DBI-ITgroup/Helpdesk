from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.save()

            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")  
    else:
        form = CustomUserRegistrationForm()

    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful!")
                return redirect("dashboard")
            else: 
                messages.error(request, "Invalid email or password!")
    else:  
        form = CustomLoginForm()
            
    return render(request, "login.html", {"form": form})

def home(request):
    return render(request, "home.html")

