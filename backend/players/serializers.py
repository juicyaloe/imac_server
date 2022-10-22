from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User
from trades.serializers import SimpleTradeSerializer
from rest_framework.validators import UniqueValidator


class PlayerSerializer(serializers.ModelSerializer):
    # Read 때는 상관 없음, Write 때는 Model 확장형으로 명시
    name = serializers.CharField(min_length=2, max_length=32, validators=[UniqueValidator(queryset=Player.objects.all())])

    # Read 때는 string 변환 용도, Write 때는 username 형식(존재 검사 O)으로 받되 필수 아님
    owner = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False)

    # 단순히 보여주기만 하는 필드, Write 때 신경쓸 필요 없음
    trading = SimpleTradeSerializer(read_only=True)

    # PATCH는 name, owner만 변경 가능(required 무시)

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

class SimplePlayerSerializer(serializers.ModelSerializer):
    # Read 용도로 단순하게 구현하는 Serializer
    class Meta:
        fields = (
            'id',
            'name',
        )
        model = Player