import imp
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from datetime import datetime
import uuid
from django.db.models.fields import UUIDField

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE','FEMALE'),
)