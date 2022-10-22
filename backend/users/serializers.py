from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.core.validators import MinLengthValidator

from players.serializers import SimplePlayerSerializer
from trades.serializers import SimpleTradeSerializer

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[MinLengthValidator(8, '비밀번호를 8자 이상 적어주세요')],
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})


class ProfilePublicSerializer(serializers.ModelSerializer):
    # read only serializer
    players = SimplePlayerSerializer(many=True, read_only=True)

    # selling = TradeSerializer(many=True, read_only=True)
    # buying = TradeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "players")


class ProfilePrivateSerializer(serializers.ModelSerializer):
    # read only serializer
    players = SimplePlayerSerializer(many=True, read_only=True)
    selling = SimpleTradeSerializer(many=True, read_only=True)
    buying = SimpleTradeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "players", 'selling', 'buying')
