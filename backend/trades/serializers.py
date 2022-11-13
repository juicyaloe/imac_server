from rest_framework import serializers
from .models import Trade
from django.contrib.auth.models import User
from players.models import Player
from rest_framework.validators import UniqueValidator
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):

    # description은 DB를 따라가지만, default, null, blank가 safe 하기 때문에 read, write 걱정 없음

    # Read 때는 string 변환 용도, Write 때는 username 형식(존재 검사 O)으로 받되 필수로 지정
    seller = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    # Read 때는 pk 변환 용도, Write 때는 pk 형식(존재 검사 O)으로 받되 필수로 지정
    # seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # Read 때는 string 변환 용도, Write 때는 username 형식(존재 검사 O)으로 받되 필수로 지정
    buyer = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    # Read 때는 pk 변환 용도, Write 때는 pk 형식(존재 검사 O)으로 받되 필수로 지정
    # buyer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # Read 때는 string 변환 용도,
    # Write 때는 name 형식(존재 검사 O, 유일성 검사)으로 받되 필수로 지정
    # targetPlayer = serializers.SlugRelatedField(slug_field='name',
    #                                             queryset=Player.objects.all(),
    #                                             validators=[UniqueValidator(queryset=Trade.objects.all())])

    # Read 때는 string 변환 용도,
    # Write 때는 pk 형식(존재 검사 O, 유일성 검사)으로 받되 필수로 지정
    targetPlayer = serializers.PrimaryKeyRelatedField(
        queryset=Player.objects.all(),
        validators=[UniqueValidator(queryset=Trade.objects.all())]
    )

    # seller가 targetPlayer를 갖고 있는지, seller가 buyer가 다른지 검사
    def validate(self, value):
        seller = getattr(self, 'instance', None).seller if 'seller' not in value else value['seller']
        buyer = getattr(self, 'instance', None).buyer if 'buyer' not in value else value['buyer']
        targetPlayer = getattr(self, 'instance', None)\
            .targetPlayer if 'targetPlayer' not in value else value['targetPlayer']

        if not targetPlayer in seller.players.all():
            raise serializers.ValidationError(
                {"targetPlayer": "seller가 가지고 있는 선수만 팔 수 있습니다"})

        if seller == buyer:
            raise serializers.ValidationError(
                {"seller": "판매자와 구매자가 같습니다"},{"buyer": "판매자와 구매자가 같습니다"}
            )

        return value

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

class SimpleTradeSerializer(serializers.ModelSerializer):
    # Read 용도로 단순하게 구현하는 Serializer
    class Meta:
        fields = ("id",)
        model = Trade
