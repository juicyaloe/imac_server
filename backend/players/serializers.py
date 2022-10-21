from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User
from trades.serializers import Simple_TradeSerializer

class PlayerSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False)
    trading = Simple_TradeSerializer(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'owner',
            'trading',
            'created_at',
            'updated_at',
        )
        model = Player