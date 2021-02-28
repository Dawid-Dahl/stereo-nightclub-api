from django.urls import path
from .views import get_is_user_logged_in

urlpatterns = [
    path('user/is-logged-in', get_is_user_logged_in),
]
