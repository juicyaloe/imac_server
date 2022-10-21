from rest_framework import serializers
from .models import Trade
from django.contrib.auth.models import User
from players.models import Player
from rest_framework.validators import UniqueValidator
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    buyer = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    targetPlayer = serializers.SlugRelatedField(slug_field='name',
                                                queryset=Player.objects.all(),
                                                validators=[UniqueValidator(queryset=Trade.objects.all())])

    class Meta:
        fields = (
            'id',
            'description',
            'seller',
            'buyer',
            'targetPlayer',
            'created_at',
            'updated_at',
        )
        model = Trade

class Simple_TradeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id",)
        model = Trade