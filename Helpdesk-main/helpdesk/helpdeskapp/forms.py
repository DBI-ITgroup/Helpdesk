from django import forms
from django.contrib.auth.models import User
from .models import Ticket


class CustomUserRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length = 50, required = True, widget = forms.TextInput(attrs = {'placeholder': 'Full Name'}))
    email = forms.EmailField(required = True, widget = forms.EmailInput(attrs = {'placeholder': 'Email Address'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}), required = True)
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm Password'}), required = True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(username = email).exists():
            raise forms.ValidationError("Email Already Exists")
        return email 
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match!")
            
class CustomLoginForm(forms.Form):
    email = forms.EmailField(required = True, widget = forms.EmailInput(attrs = {'placeholder': 'Email Address'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}), required = True)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'ticket_title', 'department', 'contact_info',
            'problem_description', 'priority_level',
            'preferred_contact_method', 'attachment'
        ]

