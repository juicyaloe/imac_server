from django.shortcuts import render
from rest_framework import generics

from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response

# Create your views here.
class ListPlayer(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class DetailPlayer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer