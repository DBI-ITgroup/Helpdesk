from .models import Ticket, CustomUser

def get_least_busy_l1_technician():
    l1_technicians = CustomUser.objects.filter(role="L1_Technician")
    
    # Get the technician with the least number of assigned tickets
    least_busy_technician = None
    min_tickets = float('inf')
    
    for technician in l1_technicians:
        assigned_tickets_count = Ticket.objects.filter(assigned_technician=technician).count()
        
        if assigned_tickets_count < min_tickets:
            min_tickets = assigned_tickets_count
            least_busy_technician = technician
    
    return least_busy_technician
