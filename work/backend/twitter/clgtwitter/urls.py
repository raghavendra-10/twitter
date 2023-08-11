# urls.py

from django.urls import path
from .views import UserRegistrationView, CustomObtainJSONWebToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomObtainJSONWebToken.as_view(), name='login'),
    # ... other URLs
]
