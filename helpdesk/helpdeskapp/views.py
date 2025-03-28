from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, CustomUser
from .forms import CustomUserRegistrationForm, CustomLoginForm, TicketForm,UserProfileUpdateForm
import uuid
from .utils import get_least_busy_l1_technician


User = get_user_model

def home(request):
    form = CustomLoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
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
                
                # Redirect based on role
                if user.role and user.role.lower() != "end-user":  
                    return redirect("admin_dashboard")  # Change to the correct admin page URL name
                else:
                    return redirect("dashboard")  

            else: 
                messages.error(request, "Invalid email or password!")
    
    else:  
        form = CustomLoginForm()
            
    return render(request, "login.html", {"form": form})

@login_required
def dashboard(request):
    tickets = Ticket.objects.filter(user=request.user)
    form = TicketForm()  # Initialize an empty form
    return render(request, 'dashboard.html', {'tickets': tickets, 'form': form})


@login_required
def add_ticket(request):
    print("📌 add_ticket view called!")  # Debugging log

    if request.method == "POST":
        print("📝 Received POST request!")  # Confirming form submission
        form = TicketForm(request.POST, request.FILES)
        
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate ticket with logged-in user
            ticket.status = 'Pending'  # Set the status to "Pending"
            ticket.ticket_number = str(uuid.uuid4())[:8].upper()  # Generate unique ticket number
            
            # Debugging logs
            print(f"✅ Saving Ticket: {ticket.ticket_title}, User: {ticket.user.email}, Ticket Number: {ticket.ticket_number}")
            
            ticket.save()
            messages.success(request, "Ticket successfully added!")
            return redirect('dashboard')  # Redirect to avoid form resubmission
        else:
            print("❌ Form is NOT valid!")
            for field, errors in form.errors.items():
                print(f"⚠️ {field}: {', '.join(errors)}")  # Print field-specific errors
            messages.error(request, "Error submitting ticket. Please check the form.")
    
    return redirect("dashboard")  # Always redirect after submission

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)  # Get tickets of logged-in user
    return render(request, 'admin.html', {'tickets': tickets})


@login_required
def settings(request):
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard')  # Redirect back to the dashboard after updating
    else:
        form = UserProfileUpdateForm(instance=request.user)  # Prepopulate the form with user data
    
    return render(request, 'dashboard.html', {'form': form})


def user_logout(request):
    logout(request)  # Properly log out the user
    messages.success(request, "You have been logged out.")
    return redirect('login')

@login_required
def admin_dashboard(request):
    return render(request, "admin.html")

@login_required
def view_tickets(request):
    if request.user.is_authenticated:
        if request.user.role == "L1_Technician":
            tickets = Ticket.objects.filter(status="Pending", assigned_technician=request.user)
        elif request.user.role == "L2_Technician":
            tickets = Ticket.objects.filter(status="Completed")
        else:
            tickets = Ticket.objects.all()  # Show all tickets for admins
        
        return render(request, "admin.html", {"tickets": tickets})

    return redirect("login")

def create_ticket(request):
    if request.method == "POST":
        ticket_title = request.POST.get("ticket_title")
        problem_description = request.POST.get("problem_description")
        priority_level = request.POST.get("priority_level")
        department = request.POST.get("department")

        assigned_technician = get_least_busy_l1_technician()

        ticket = Ticket.objects.create(
            ticket_title=ticket_title,
            department=department,
            contact_info=request.user.email,
            problem_description=problem_description,
            priority_level=priority_level,
            preferred_contact_method="Email",
            user=request.user,
            status="Pending",
            assigned_technician=assigned_technician if assigned_technician else None
        )

        return redirect("view_tickets")

    return render(request, "admin.html")