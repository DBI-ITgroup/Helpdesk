import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('End-User', 'End-User'),
        ('Technician', 'Technician'),
        ('Administrator', 'Administrator'),
    ]
    
    full_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'role']
    
    def __str__(self):
        return f"{self.full_name} ({self.role})"

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    ticket_title = models.CharField(max_length=255)
    department = models.CharField(
        max_length=100, choices=[
            ('IT', 'IT'),
            ('HR', 'HR'),
            ('Finance', 'Finance'),
        ]
    )
    contact_info = models.CharField(max_length=255)
    problem_description = models.TextField()
    priority_level = models.CharField(
        max_length=50, choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ]
    )
    preferred_contact_method = models.CharField(
        max_length=50, choices=[
            ('Email', 'Email'),
            ('Phone', 'Phone'),
        ]
    )
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    date_created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    status = models.CharField(max_length=20, default='Pending')  


    def save(self, *args, **kwargs):
        if not self.ticket_number:  
            self.ticket_number = str(uuid.uuid4())[:8].upper()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_number} - {self.ticket_title}"