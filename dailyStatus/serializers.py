from .models import Journy
from rest_framework import serializers

class JournySerializer(serializers.ModelSerializer):
    class Meta:
        model= Journy
        fields= "__all__"

        