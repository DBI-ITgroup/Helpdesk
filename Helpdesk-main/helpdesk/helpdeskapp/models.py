from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_number = models.CharField(max_length=20, unique=True)
    ticket_title = models.CharField(max_length=255)
    department = models.CharField(max_length=100, choices=[
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('Support', 'Support')
    ])
    contact_info = models.CharField(max_length=255)
    problem_description = models.TextField()
    priority_level = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])
    preferred_contact_method = models.CharField(max_length=50, choices=[
        ('Email', 'Email'),
        ('Phone', 'Phone')
    ])
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    date_created_on = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)  # Track who created the ticket

    def __str__(self):
        return f"{self.ticket_number} - {self.ticket_title}"
