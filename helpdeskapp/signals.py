from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'L1_Technician':
            # Assign the 'view_pending_tickets' permission to L1 Technicians
            permission = Permission.objects.get(codename='view_pending_tickets')
            instance.user_permissions.add(permission)

        elif instance.role == 'L2_Technician':
            # Assign the 'view_escalated_tickets' permission to L2 Technicians
            permission = Permission.objects.get(codename='view_escalated_tickets')
            instance.user_permissions.add(permission)

        elif instance.role == 'Administrator':
            # Admins typically get all permissions (for example, all tickets)
            permissions = Permission.objects.all()
            instance.user_permissions.set(permissions)

        # Additional role-based permissions can be added here

