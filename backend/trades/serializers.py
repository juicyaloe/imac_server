from rest_framework import serializers
from .models import Trade
from django.contrib.auth.models import User

class TradeSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    buyer = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = (
            'id',
            'description',
            'seller',
            'buyer',
        )
        model = Trade