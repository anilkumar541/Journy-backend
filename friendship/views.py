from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user_management.models import CustomUser
from .models import FriendRequest
from .serializers import FriendRequestSerializer

#Send friend request
class SendFriendRequest(APIView):

    permission_classes= [IsAuthenticated]

    def post(self, request, format= None):
        to_user_email= request.data.get("email")
        to_user= get_object_or_404(CustomUser, email= to_user_email)
        friend_request, created= FriendRequest.objects.get_or_create(from_user= request.user, to_user= to_user)
        if created:
            return Response({"status": "Friend request sent"}, status= status.HTTP_201_CREATED)
        else:
            return Response({"status": "Friend request already sent"}, status= status.HTTP_400_BAD_REQUEST)


#Accept friend request
class AcceptFriendRequest(APIView):

    permission_classes= [IsAuthenticated]

    def post(self, request, format= None):
        request_id= request.data.get("request_id")
        friend_request= get_object_or_404(FriendRequest, id= request_id, to_user= request.user)
        from_user= friend_request.from_user
        request.user.add_friend(from_user)
        friend_request.delete()
        return Response({"status": "Friend request accepted"}, status= status.HTTP_200_OK)


#Reject friend request
class RejectFriendRequest(APIView):

    permission_classes= [IsAuthenticated]

    def post(self, request, format= None):
        request_id= request.data.get("request_id")
        friend_request= get_object_or_404(FriendRequest, id=request_id, to_user= request.user)
        friend_request.delete()
        return Response({"status": "Friend request rejected"}, status= status.HTTP_200_OK)
        