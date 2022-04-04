from collections import UserDict
from xml.etree.ElementInclude import FatalIncludeError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import uuid
from django.db.models.fields import UUIDField

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )



# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, first_name, last_name,user_name, email, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not user_name:
            raise ValueError('user must have a user_name ')
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(self.db)
        return user

    def create_superuser(self, first_name, last_name,user_name, email, password=None):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            email = self.normalize_emai(email),
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin =True
        user.save(using = self.db)
        return user

    def create_vendor(self,email,password=None):
        if not email:
            raise ValueError('Vendor must have a email address')

        vendor = self.model(
            email = self.normalize_email(email),
        )    

        vendor.is_admin = False
        vendor.is_active =True
        vendor.is_verifies = False
        vendor.is_staff = True
        vendor.is_superadmin = False
        vendor.set_password(password)
        vendor.save(using=self.db)
        return vendor



class CustomUser(AbstractBaseUser):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        user_name = models.CharField(max_length=50, unique=True)
        email = models.EmailField(max_length=50, unique=True)
        phone_number = models.CharField(max_length=60)

        # required
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(auto_now_add=True)
        is_admin = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_superadmin = models.BooleanField(default=False)


        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['user_name','first_name','last_name']

        objects = CustomUserManager()

        def has_perm(self,perm, obj=None):
            return self.is_admin

        def has_module_perms(self, add_label):
            return True

        def __str__(self):
            return self.email



class Address(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    address_line_1=models.CharField(max_length=100)
    address_line_2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip_code=models.BigIntegerField()
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    landmark=models.CharField(max_length=50)
    
    default=models.BooleanField(default=False)

    class Meta:
        verbose_name    =    "Address"
        verbose_name_plural =   "Addresses"
    
