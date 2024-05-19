from rest_framework import serializers
from .models import CustomUser
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util


class UserResgistrationSerializer(serializers.ModelSerializer):
    password= serializers.CharField(style= {"input_type": "password"}, write_only= True)
    confirm_password= serializers.CharField(style= {"input_type": "password"}, write_only= True)

    class Meta:
        model= CustomUser
        fields= ["fullname", "email", "password", "confirm_password"]
        extra_kwargs= {
            "password": {"write_only": True},
            "fullname": {"required": True},
            "email": {"required": True}
        }

    def validate(self, data):
        password= data.get('password')
        confirm_password= data.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("Password does not match...")
        return data


    def create(self, validated_data):
        password= validated_data.pop("confirm_password") #get the password
        user= CustomUser.objects.create_user(**validated_data)
        user.set_password(password) #hash the password
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=200)
    class Meta:
        model= CustomUser
        fields= ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields= ["id", "fullname", "email", "date_joined"]


class ChangePasswordSerializer(serializers.Serializer):
    password= serializers.CharField(max_length= 35, style= {"input_type": "password"}, write_only= True)
    confirm_password= serializers.CharField(max_length= 35, style= {"input_type": "password"}, write_only= True)

    class Meta:
        fields= ["password", "confirm_password"]

    def validate(self, data):
        password= data.get("password")
        confirm_password= data.get("confirm_password")
        user= self.context.get("user")

        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm_password does not match")
        if user:
            user.set_password(password)
            user.save()
        return data

    def create(self, validated_data):
        # Create and return a new instance of YourModel using the validated data
        confirm_password= validated_data.pop("confirm_password")
        return CustomUser.objects.create(**validated_data)


class SendForgotPasswordEmailSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length= 100)

    class Meta:
        fields= ["email"]

    def validate(self, data):
        email= data.get("email")
        if CustomUser.objects.filter(email= email).exists():
            user= CustomUser.objects.get(email= email)
            user_id= user.id
            encoded_user_id= urlsafe_base64_encode(force_bytes(user_id))
            token= PasswordResetTokenGenerator().make_token(user)
            link= "http://localhost:3000/api/user/forgot_password/"+ encoded_user_id + "/" + token
            body= "Click link to reset password" + link
            data={
                "subject": "Forgot password",
                "body": body,
                "to_email": user.email
            }
            # from user_management.utils import send_email_
            Util.send_email(data)
            # send_email_(data)

            return data
        else:
            raise serializers.ValidationError("You are not a registered user")
        

class ForgotPasswordUpdateSerializer(serializers.Serializer):
    password= serializers.CharField(max_length= 35, style= {"input_type": "password"}, write_only= True)
    confirm_password= serializers.CharField(max_length= 35, style= {"input_type": "password"}, write_only= True)

    class Meta:
        fields= ["password", "confirm_password"]

    def validate(self, data):
        try:
            password= data.get("password")
            confirm_password= data.get("confirm_password")
            encoded_user_id= self.context.get("encoded_user_id")
            token= self.context.get("token")

            if password != confirm_password:
                raise serializers.ValidationError("Password and confirm_password does not match")
            
            id= smart_str(urlsafe_base64_decode(encoded_user_id))
            user= CustomUser.objects.get(id= id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or expired")
                

            if user:
                user.set_password(password)
                user.save()
            return data
        except DjangoUnicodeDecodeError as error:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token is not valid or expired")
            
            
    

    # def create(self, validated_data):
    #     # Create and return a new instance of YourModel using the validated data
    #     confirm_password= validated_data.pop("confirm_password")
    #     return CustomUser.objects.create(**validated_data)    

            