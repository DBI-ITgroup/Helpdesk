from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('logout/', views.user_logout, name='logout'),

]
