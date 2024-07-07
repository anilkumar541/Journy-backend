from django.urls import path
from .views import SendFriendRequest, AcceptFriendRequest, RejectFriendRequest

urlpatterns = [
    path('send_friend_request/', SendFriendRequest.as_view(), name='send_friend_request'),
    path('accept_friend_request/', AcceptFriendRequest.as_view(), name='accept_friend_request'),
    path('reject_friend_request/', RejectFriendRequest.as_view(), name='reject_friend_request'),
]