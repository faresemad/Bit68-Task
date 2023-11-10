from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserLoginSerializer, UserRegistrationSerializer


@api_view(["POST"])
def user_registration(request):
    """User Registration

    Args:
        {
            "username": "test",
            "email": "test@example.com",
            "password": "test1234"
        }

    Returns:
        {
            "id": 1,
            "username": "test",
            "email": "test@example.com",
        }
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    """User Login

    Args:
        {
            "username": "test",
            "password": "test1234"
        }

    Returns:
        {
            "token" : "<Token>"
        }
    """
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
