from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
        )
        model = Player