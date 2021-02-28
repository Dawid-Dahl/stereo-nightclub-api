from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer


class CustomUserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        print("SERIALIZER", serializer)
        if serializer.is_valid():
            user = serializer.save()
            print("USER", user)
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
