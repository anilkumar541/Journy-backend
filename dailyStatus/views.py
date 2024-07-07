from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from dailyStatus.models import Journy
from dailyStatus.serializers import JournySerializer
from django.db.models import Q
from rest_framework import generics
from .pagination import CustomLimitOffsetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class JournyList(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request, format= None):
        user = request.user
        journy= Journy.objects.filter(
            Q(user = user) | #user's own post means (private post)
            Q(privacy= "Public") | #public post
            Q(privacy= "Friends Only", user__friends__in=[user]) # Friends-only posts
            ).distinct().order_by("-created")
        serialzer= JournySerializer(journy, many=True)
        return Response(serialzer.data)

    def post(self, request, format= None):
        serialzer= JournySerializer(data= request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


#To fetch all the public Journey
class AllJournyList(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request, format= None):
        all_journey= Journy.objects.all().order_by("-created")
        serializer= JournySerializer(all_journey, many= True)
        return Response(serializer.data)

