from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import permissions
from rest_framework.views import exceptions

# Create your views here.

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"Token": token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileSerializer

    def validate(self, request):
        if not "username" in request.data:
            raise exceptions.ParseError("username 값이 없습니다.")
        username = request.data['username']

        queryset = User.objects.filter(username=username).first()
        if not queryset:
            raise exceptions.ParseError("해당 User는 없습니다.")
        return queryset

    def get(self, request):
        queryset = self.validate(request)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


