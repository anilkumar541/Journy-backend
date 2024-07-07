from rest_framework import serializers
from friendship.models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model= FriendRequest
        fields= ["id", "from_user", "to_user", "timestamp"]
        