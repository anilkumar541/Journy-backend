from django.db import models
from user_management.models import CustomUser

class Journy(models.Model):
    HOW_WAS_THE_DAY = [
    ("Excellent", "Excellent"),
    ("Good", "Good"),
    ("Ok", "Ok"),
    ("Bad", "Bad"),
    ]

    PRIVACY_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Friends only', 'Friends only'),
    ]

    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mood= models.CharField(choices= HOW_WAS_THE_DAY, max_length=10, default='Good')
    notes= models.TextField()
    privacy= models.CharField(choices=PRIVACY_CHOICES, max_length=12, default='PR')
    created= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

    # Optional fields for media files
    image = models.ImageField(upload_to='journey_images/', blank=True, null=True)
    video = models.FileField(upload_to='journey_videos/', blank=True, null=True)

    class Meta:
        ordering = ['-created']
        db_table = 'journeys'

        