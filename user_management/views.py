from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import (UserResgistrationSerializer, LoginSerializer, UserProfileSerializer, ChangePasswordSerializer, SendForgotPasswordEmailSerializer, ForgotPasswordUpdateSerializer)
from user_management.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes= [UserRenderer]

    # def get(self, request, format= None):
    #     return Response({"msg": "get"})
    
    def post(self, request, format= None):
        serializer= UserResgistrationSerializer(data= request.data)
        if serializer.is_valid():
            user= serializer.save()
            tokens= get_tokens_for_user(user)
            return Response({"token": tokens, "Message": "Registration successfull"}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST )


class LoginView(APIView):
    def post(self, request, format= None):
        # request.session["hello"]= "okkk"
        # print(request.session["hello"])
        serializer= LoginSerializer(data= request.data)
        if serializer.is_valid():
            email= serializer.data.get("email")
            password= serializer.data.get("password")
            user= authenticate(email= email, password= password)
            if user:
                tokens= get_tokens_for_user(user)
                return Response({"token": tokens, "Message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"errors": {"non_field_errors": ["Email or Password is not valid"]}}, status=status.HTTP_404_NOT_FOUND)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# USER PROFILE
class UserProfileView(APIView):
    renderer_classes= [UserRenderer]
    permission_classes= [IsAuthenticated]

    def get(self, request, format= None):
        serializer= UserProfileSerializer(request.user)
        if serializer:
            return Response({"data": serializer.data}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)


# Change password
class ChangePasswordView(APIView):
    renderer_classes= [UserRenderer]
    permission_classes= [IsAuthenticated]

    def post(self, request, format= None):
        serializer= ChangePasswordSerializer(data= request.data, context= {"user": request.user})
        # print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Password change successfull"}, status= status.HTTP_200_OK)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



class SendForgotPasswordEmailView(APIView):
    renderer_classes= [UserRenderer]

    def post(self, request, format= None):
        serializer= SendForgotPasswordEmailSerializer(data= request.data)
        if serializer.is_valid():
            return Response({"msg": "Password reset link sent on your mail id"}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class ForgotPasswordUpdateView(APIView):
    renderer_classes= [UserRenderer]

    def post(self, request, encoded_user_id, token, format= None):
        serializer= ForgotPasswordUpdateSerializer(data= request.data, context= {"encoded_user_id": encoded_user_id, "token": token})

        if serializer.is_valid():
            return Response({"msg": "Password Reset successfully"}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


