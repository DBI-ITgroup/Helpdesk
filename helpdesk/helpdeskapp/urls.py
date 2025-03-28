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
]
