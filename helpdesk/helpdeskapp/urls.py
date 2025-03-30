from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.user_login, name='login'),  # User login
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('add_ticket/', views.add_ticket, name='add_ticket'),  # Add a ticket
    path('my_tickets/', views.my_tickets, name='my_tickets'),  # View user's tickets
    path('logout/', views.user_logout, name='logout'),  # User logout
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),  # Admin dashboard
    path('tickets/', views.view_tickets, name='view_tickets'),  # View all tickets
    path("technician-dashboard/", views.technician_dashboard, name="technician_dashboard"),  # Technician dashboard
    path("user/settings/", views.settings, name="user_settings"), #user settings 

     # Ticket action URLs
    path('ticket/<int:id>/accept/', views.accept_ticket, name='accept_ticket'),
    path('ticket/<int:id>/request-info/', views.request_info, name='request_info'),
    path('ticket/<int:id>/escalate/', views.escalate_ticket, name='escalate_ticket'),
    path('ticket/<int:id>/complete/', views.complete_ticket, name='complete_ticket'),
]
