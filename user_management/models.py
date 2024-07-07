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

    friends = models.ManyToManyField('self', symmetrical=False, related_name='friends_with', blank=True)
    #The symmetrical=False parameter means that if user A is friends with user B, it doesn’t automatically mean user B is friends with user A (though in many social apps, you might want this to be symmetrical).

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    objects = CustomUserManager()


    def __str__(self):
        return self.email
    
    def get_fullname(self):
        return f"{self.fullname}"
        
    def add_friend(self, friend):
        self.friends.add(friend)
        friend.friends.add(self)

    def remove_friend(self, friend):
        self.friends.remove(friend)
        friend.friends.remove(self)

    def is_friend(self, user):
        return self.friends.filter(id=user.id).exists()
        