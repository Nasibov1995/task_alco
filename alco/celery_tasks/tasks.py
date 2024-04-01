from celery import shared_task
from datetime import timedelta
from main.models import BlockedIP
from django.db.models.functions import Now
from main.models import CustomUser

@shared_task()
def unblock_ip():
    try:
        
        
        ip_adresses = BlockedIP.objects.filter(timestamp__lte = Now() - timedelta(seconds=50))
        ip_address = 0
        for ip in ip_adresses:
            ip_address = ip.blocked_ip_address
            
        user_with_ip = CustomUser.objects.filter(ip_address=ip_address, is_active=False)
        
        for user_with_ip in user_with_ip:
            user_with_ip.is_active = True
            user_with_ip.save()
            

        BlockedIP.objects.filter(timestamp__lte = Now() - timedelta(seconds=50)).delete()
        
        return f"IP address {ip_address} unblocked successfully"
    except BlockedIP.DoesNotExist:
        return f"IP address {ip_address} was not found in the blocked list"

