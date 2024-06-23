from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from dailyStatus.models import Journy
from dailyStatus.serializers import JournySerializer


class JournyList(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request, format= None):
        journy= Journy.objects.all()
        serialzer= JournySerializer(journy, many=True)
        return Response(serialzer.data)

    def post(self, request, format= None):
        serialzer= JournySerializer(data= request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


