import uuid
from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link ticket to user
    status = models.CharField(max_length=20, default='Pending')  # New status field with default value


    def save(self, *args, **kwargs):
        if not self.ticket_number:  # Generate unique ticket number
            self.ticket_number = str(uuid.uuid4())[:8].upper()  # Example: A1B2C3D4
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_number} - {self.ticket_title}"
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    contact_method = models.CharField(max_length=50, choices=[('Email', 'Email'), ('Phone', 'Phone')])

    def __str__(self):
        return self.user.username