from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Ticket

@receiver(post_save, sender=CustomUser)
def assign_permissions(sender, instance, created, **kwargs):
    if created:  # Assign permissions only when a user is created
        content_type = ContentType.objects.get_for_model(Ticket)

        if instance.role == 'L1_Technician':
            permission = Permission.objects.get(content_type=content_type, codename='view_pending_tickets')
            instance.user_permissions.add(permission)

        elif instance.role == 'L2_Technician':
            permission = Permission.objects.get(content_type=content_type, codename='view_completed_tickets')
            instance.user_permissions.add(permission)
