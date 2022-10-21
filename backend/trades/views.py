from django.shortcuts import render
from rest_framework import generics

from .models import Trade
from .serializers import TradeSerializer
from rest_framework.response import Response

# Create your views here.
class ListTrade(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class DetailTrade(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
