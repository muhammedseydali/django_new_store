from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

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

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"