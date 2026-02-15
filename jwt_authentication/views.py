from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# View => a function or class that handles an HTTP request and returns an HTTP response
# Class based view handle different HTTP methods(get post put delete)
# APIVIEW auto handles JSON suppports auth/permission easy to use with serializers
# Response object rendor JSON,XML unlike HttpResponse, HTTP status codes


class RegisterView(APIView):
    # even unauthenticated users can hit this endpoint -> need for signup
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Takes incoming JSON from client maps to serializer
        serializer = RegisterSerializer(data=request.data)
        # validates fields(username unique, email unique, password present)
        # Raises 400 Bad Request automatically if invalid
        serializer.is_valid(raise_exception=True)
        # calls the create() method in RegisterSerializer -> creates the user in DB
        user = serializer.save()
        # Return JSON containing 
        return Response({
            "message": "User created successfully",
            "user" : UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
# on POST with username + password it returns a custom token
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

class ProfileView(APIView):
    # only logged-on users with valid JWT can access
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        return Response(UserSerializer(request.user).data)

# JWT logging out isn't automatic like with sessions
# Access token expire naturally in ex 15 minutes
# blacklisting the refresh token prevents from getting new access tokens
class LogoutView(APIView):
    # only logged-in users with valid access token can log out
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # clients must send the refresh token in the body of the POST request
        # request.data["refresh"] front end sends the refresh token in JSON
        token = RefreshToken(request.data["refresh"])
        token.blacklist()
        return Response({
            "message": "Logged Out"
        })