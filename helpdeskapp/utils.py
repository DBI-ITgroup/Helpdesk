from django.db.models import Count
from .models import CustomUser, Ticket

def get_least_busy_l1_technician():
    """
    Finds the L1 Technician with the least number of assigned tickets.
    """
    # Annotate L1 technicians with the count of assigned tickets
    l1_technicians = CustomUser.objects.filter(role="L1_Technician") \
        .annotate(assigned_tickets_count=Count('assigned_tickets')) \
        .order_by('assigned_tickets_count')  # Order by the count in ascending order

    # Return the technician with the least tickets assigned (first in the ordered queryset)
    return l1_technicians.first()  # This will return None if there are no technicians

def get_least_busy_l2_technician():
    """
    Finds the L2 Technician with the least number of assigned tickets.
    """
    # Annotate L2 technicians with the count of assigned tickets
    l2_technicians = CustomUser.objects.filter(role='L2_Technician') \
        .annotate(assigned_tickets_count=Count('assigned_tickets')) \
        .order_by('assigned_tickets_count')  # Order by the count in ascending order

    # Return the technician with the least tickets assigned (first in the ordered queryset)
    return l2_technicians.first()  # This will return None if there are no technicians
