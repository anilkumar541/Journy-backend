from django.db import models
from django.conf import settings

class FriendRequest(models.Model):
    from_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_request", on_delete=models.CASCADE)
    to_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_request", on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return f"{self.from_user} to {self.to_user}"
        