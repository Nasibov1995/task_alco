from django.dispatch import receiver
from django.db.models.signals import post_save
from main.models import BlockedIP,CustomUser

@receiver(post_save,sender=BlockedIP)
def register_user(sender,created=False,instance=None,**kwargs):
    if created:
        ip_adresses = BlockedIP.objects.all()
        ip_address = 0
        for ip in ip_adresses:
            ip_address = ip.blocked_ip_address
            
        # Check if the IP address is associated with any active user
        user_with_ip = CustomUser.objects.filter(ip_address=ip_address, is_active=True)
        for user_with_ip in user_with_ip:
            user_with_ip.is_active = False
            user_with_ip.save()
            
    print("Signal ise dusdu")