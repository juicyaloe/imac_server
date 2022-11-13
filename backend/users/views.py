from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfilePublicSerializer, ProfilePrivateSerializer
from rest_framework import permissions
from rest_framework.views import exceptions

from .permissions import PrivateOnlyMyToken

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


class ProfilePublicView(generics.ListAPIView):
    queryset = User.objects.exclude(id=1)
    serializer_class = ProfilePublicSerializer


class ProfilePrivateView(generics.GenericAPIView):
    permission_classes = [PrivateOnlyMyToken]
    serializer_class = ProfilePrivateSerializer

    def input_permission(self, request):
        if "username" not in request.data:
            raise exceptions.ParseError("username 값이 없습니다.")
        username = request.data['username']

        if username == 'admin':
            raise exceptions.ParseError("admin은 조회할 수 없습니다.")

        queryset = User.objects.filter(username=username).first()
        if not queryset:
            raise exceptions.ParseError("해당 User는 없습니다.")
        return queryset

    def get(self, request):
        queryset = self.input_permission(request)
        self.check_object_permissions(self.request, queryset)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request):
    #     queryset = self.input_permission(request)
    #     serializer = self.get_serializer(queryset, data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

