from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=["id", "email", "fullname", "last_login", "is_superuser", "date_joined"]
    
