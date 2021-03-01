from django.urls import path
from .views import CustomUserRegistration, BlackListToken

urlpatterns = [
    path('register/', CustomUserRegistration.as_view()),
    path("logout/blacklist/", BlackListToken.as_view())
]
