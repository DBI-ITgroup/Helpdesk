from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
import random
import string

def generate_ticket_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

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

def dashboard(request):
    return render(request, "dashboard.html")

def home(request):
    return render(request, "home.html")

def user_logout(request):
    return render(request, "login.html")

@login_required
def dashboard(request):
    form = TicketForm()
    return render(request, 'dashboard.html', {'form': form})

@login_required
def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.ticket_number = generate_ticket_number()
            ticket.email = request.user
            ticket.save()
            print("Ticket Saved:", ticket)  # Debugging
            return redirect('dashboard')
        else:
            print("Form Errors:", form.errors)  # Debugging
    return render(request, 'add_ticket.html', {'form': form})



@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(email=request.user)
    return render(request, 'my_tickets.html', {'tickets': tickets})

@login_required
def settings(request):
    return render(request, 'settings.html')
