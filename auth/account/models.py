from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    '''
    create user-Manger class
    '''
    def create_superuser(self, email, password):
        user=self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser,PermissionsMixin):
    '''
    create custom user modal
    '''
    first_name=models.CharField("User First Name",max_length=50,null=False,blank=False)
    last_name=models.CharField("User Last Name", max_length=50, null=False, blank=False)
    email = models.EmailField("User Email", null=False, blank=False,unique=True, error_messages={"unique":"OOPS,This Email is Already Registered"})
    phone = models.IntegerField("User Phone", null=True, blank=True, unique=True, error_messages={"unique":"this mobile number is already exist"})
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects=UserManager()
    # notice the absence of a "Password field", that is built in.
    USERNAME_FIELD = 'email'

