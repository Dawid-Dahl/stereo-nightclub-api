from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from users.serializers import CustomUserSerializer
from rest_framework import status
from django.db.utils import IntegrityError
from django.contrib import messages


@api_view(["GET"])
def get_is_user_logged_in(request):
    print(request.user)
    is_authenticated = request.user.is_authenticated
    return Response({"isUserLoggedIn": is_authenticated})


class CustomUserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = CustomUserSerializer(data=request.data)
            print(1)
            if serializer.is_valid():
                print(2, serializer)
                user = serializer.save()
                print("USER", user)
                if user:
                    json = serializer.data
                    return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
