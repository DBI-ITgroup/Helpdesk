import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('End-User', 'End-User'),
        ('Technician', 'Technician'),
        ('Administrator', 'Administrator'),
        ('L1_Technician', 'L1_Technician'),
        ('L2_Technician', 'L2_Technician'),
        ('CAB', 'CAB'),
    ]
    
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'role']
    
    def __str__(self):
        return f"{self.full_name} ({self.role})"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    CONTACT_METHOD_CHOICES = [
        ('Email', 'Email'),
        ('Phone', 'Phone'),
    ]

    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
    ]

    ticket_id = models.AutoField(primary_key=True)
    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    ticket_title = models.CharField(max_length=255)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    contact_info = models.CharField(max_length=255)
    problem_description = models.TextField()
    priority_level = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    preferred_contact_method = models.CharField(max_length=50, choices=CONTACT_METHOD_CHOICES)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    date_created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    assigned_technician = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="assigned_tickets"
    )

    class Meta:
        permissions = [
            ("view_pending_tickets", "Can view pending tickets"),
            ("view_completed_tickets", "Can view completed tickets"),
        ]

    def assign_technician(self):
        """Automatically assign the ticket to the least busy L1 Technician."""
        if not self.assigned_technician:
            from helpdeskapp.models import CustomUser  # Avoid circular import

            least_busy_technician = CustomUser.objects.filter(role="L1_Technician") \
                .annotate(ticket_count=Count('assigned_tickets')) \
                .order_by('ticket_count') \
                .first()
            
            if least_busy_technician:
                self.assigned_technician = least_busy_technician

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = str(uuid.uuid4())[:8].upper()

        self.assign_technician()  # Assign technician if not assigned
        super().save(*args, **kwargs)

    def __str__(self):
        assigned_to = self.assigned_technician.full_name if self.assigned_technician else "Unassigned"
        return f"{self.ticket_number} - {self.ticket_title} (Assigned to: {assigned_to})"