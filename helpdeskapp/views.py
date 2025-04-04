from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, CustomUser
from .forms import CustomUserRegistrationForm, CustomLoginForm, TicketForm,UserProfileUpdateForm
import uuid
from .utils import get_least_busy_l1_technician
from .utils import get_least_busy_l2_technician
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied



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
                
                # Redirect based on the role
                if user.role == "End-User":
                    return redirect("dashboard")  # End-users go to their dashboard
                elif user.role == "L1_Technician" or user.role == "L2_Technician":
                    return redirect("technician_dashboard")  # Redirect L1/L2 Technicians to their dashboard
                else:
                    return redirect("admin_dashboard")  # Admin users go to the admin dashboard

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
            if not request.user.has_perm("helpdeskapp.view_pending_tickets"):
                return render(request, "base.html", {"error_message": "You do not have permission to view pending tickets."})

            tickets = Ticket.objects.filter(status="Pending", assigned_technician=request.user)
            return render(request, "technician_dashboard.html", {"tickets": tickets})

        elif request.user.role == "L2_Technician":
            if not request.user.has_perm("helpdeskapp.view_escalated_tickets"):
                return render(request, "base.html", {"error_message": "You do not have permission to view escalated tickets."})

            tickets = Ticket.objects.filter(status="Escalated", assigned_technician=request.user)
            return render(request, "technician_dashboard.html", {"tickets": tickets})

        else:
            if not request.user.is_staff:
                return render(request, "base.html", {"error_message": "Access denied!"})

            tickets = Ticket.objects.all()  # Admins can see all tickets
            return render(request, "admin.html", {"tickets": tickets})

    return redirect("login")


@login_required 
def technician_dashboard(request):
    if request.user.role == "L1_Technician" : 
        if not request.user.has_perm("helpdeskapp.view_pending_tickets"):
            #raise PermissionDenied  # Block unauthorized access
            return render(request, "base.html", {"error_message": "You do not have permission to view this page."})


        tickets = Ticket.objects.filter(assigned_technician=request.user)
        return render(request, "technician_dashboard.html", {"tickets": tickets})

    #messages.error(request, "Unauthorized access!")
    #return redirect("dashboard") 
    return render(request, "base.html", {"error_message": "Unauthorized access!"})



@login_required
def accept_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.status = "In Progress"
    ticket.save()
    return redirect("technician_dashboard")
@login_required
def request_info(request, id):
    ticket = get_object_or_404(Ticket,id=id)
    ticket.status = "Waiting for Info"
    ticket.save()
    return redirect("technician_dashboard")
@login_required
def escalate_ticket(request,id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.status = "Escalated"
    ticket.save()
    return redirect("technician_dashboard")
@login_required
def complete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.status = "Completed"
    ticket.save()
    return redirect("technician_dashboard")

@login_required
def l2_technician_dashboard(request):
    if request.user.role == "L2_Technician":
        # Ensure you're filtering by 'Escalated' status and assigned technician
        escalated_tickets = Ticket.objects.filter(status="Escalated", assigned_technician=request.user)
        
        context = {
            "escalated_tickets": escalated_tickets,
        }
        return render(request, "l2_technician_dashboard.html", context)
    else:
        messages.error(request, "Unauthorized access!")
        return redirect("dashboard")

