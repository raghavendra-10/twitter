# views.py

from rest_framework import generics, permissions
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class CustomObtainJSONWebToken(ObtainJSONWebToken):
    # Customize if needed
    pass
