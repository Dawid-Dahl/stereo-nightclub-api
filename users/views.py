from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@api_view(["GET"])
def get_is_user_logged_in(request):
    print(request.user)
    is_authenticated = request.user.is_authenticated
    return Response({"isUserLoggedIn": is_authenticated})
