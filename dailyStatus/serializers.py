from .models import Journy
from rest_framework import serializers

class JournySerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    class Meta:
        model= Journy
        fields= ("id", "user", "mood", "notes", "privacy", "created", "updated", "image", "video")

    # def get_user(self, obj):
    #     return obj.user.get_fullname()
