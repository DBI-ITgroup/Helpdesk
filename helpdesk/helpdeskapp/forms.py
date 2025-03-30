from django import forms
from .models import Ticket, CustomUser

from django import forms
from .models import CustomUser

class CustomUserRegistrationForm(forms.ModelForm):
    
    full_name = forms.CharField(
        max_length=50, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), 
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), 
        required=True
    )
    role = forms.CharField(
        initial='End-User', 
        widget=forms.HiddenInput(), 
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():  # Fixed incorrect field
            raise forms.ValidationError("Email Already Exists")
        return email 

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match!")

        return cleaned_data

    def save(self, commit=True):
     user = super().save(commit=False)
     user.username = self.cleaned_data["email"]  
     user.role = "End-User"
     user.set_password(self.cleaned_data["password"])

     if commit:
        user.save()

     return user



class CustomLoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'ticket_title', 'department', 'contact_info', 
            'problem_description', 'priority_level', 
            'preferred_contact_method', 'attachment'
        ]


    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Email already exists!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', "Passwords do not match!")
        return cleaned_data

class UserSettingsForm(forms.ModelForm):
    full_name = forms.CharField(max_length = 50, required = True, widget = forms.TextInput(attrs = {'placeholder': 'Full Name'}))
    new_password = forms.CharField(required = False, widget = forms.PasswordInput(attrs = {'placeholder': 'New Password'}))
    confirm_password = forms.CharField(required = False, widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm New Password'}))
    
    class Meta:
        model = CustomUser
        fields = ['full_name']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password or confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
            if len(new_password) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name, user.last_name = self.cleaned_data['full_name'].split(" ", 1) if " " in self.cleaned_data['full_name'] else (self.cleaned_data['full_name'], "")

        if self.cleaned_data.get("new_password"):
            user.set_password(self.cleaned_data["new_password"])

        if commit:
            user.save()
        return user