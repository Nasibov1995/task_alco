# admin.py
from django.contrib import admin
from .models import CustomUser,BlockedIP

@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ('blocked_ip_address', 'timestamp')
    search_fields = ('blocked_ip_address',)
    


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email','is_active','is_staff','last_login')
    search_fields = ['ip_address','username','email']
    list_editable = ['is_active','is_staff']
    def save_model(self, request, obj, form, change):
        obj.ip_address = request.META.get('REMOTE_ADDR')
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)