from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False, null= True, blank= True)
    is_active = models.BooleanField(default=True, null= True, blank= True)
    date_joined = models.DateTimeField(auto_now= True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    objects = CustomUserManager()


    def __str__(self):
        return self.email