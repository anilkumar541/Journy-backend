from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=["id", "email", "fullname", "last_login", "is_superuser", "date_joined", "display_friends"]
    
    def display_friends(self, obj):
        return ", ".join([friend.fullname for friend in obj.friends.all()])
    display_friends.short_description= "Friends"
