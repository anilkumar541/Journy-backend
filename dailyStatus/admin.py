from django.contrib import admin
from dailyStatus.models import Journy


@admin.register(Journy)
class JournyAdmin(admin.ModelAdmin):
    list_display=["id", "user", "mood", "notes", "privacy", "created", "updated"]
    

