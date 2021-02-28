from django.urls import path
from .views import CustomUserRegistration, get_is_user_logged_in

urlpatterns = [
    path('register/', CustomUserRegistration.as_view()),
    path('is-logged-in/', get_is_user_logged_in)
]
