from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts import serializers
from accounts.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    # Use for returning custom pair as response 
    # when successful login is performed
    serializer_class = CustomTokenObtainPairSerializer


class RegisterAPI(APIView):
    #instantiating serializer
    serializer_class = serializers.UserRegisterSerializer

    #Use to create user either admin or normal user
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #Generating token from the particular user
            #With token can access APIs
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user' : serializer.data
                
            }
            #return tokens and user data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This APIView will blacklist the refresh token
#Although access token can still be used if valid
class LogoutAPI(APIView):
    def post(self, request, format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception  as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
