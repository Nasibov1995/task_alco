
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email,password=None):
        if not email:
            raise ValueError("Please enter an email address")
        if not username:
            raise ValueError("Please enter a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,first_name,last_name,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    last_login = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']


    def has_perm(self,has_perm,obj=None):
        return self.is_superuser

    def has_module_perms(self,add_label=None):
        return True

    def __str__(self):
        return self.username
    
    
    
    
class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True,db_index=True)
    
    
    def formatted_created_at(self):
        return self.timestamp.astimezone(timezone.now())