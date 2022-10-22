from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import exceptions

class PrivateOnlyMyToken(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if 'Authorization' not in request.headers:
            raise exceptions.ParseError("Authorization 필드가 없습니다")
        try:
            header_token = request.headers['Authorization'].split(' ')[1]
            return obj == Token.objects.get(key=header_token).user
        except:
            raise exceptions.ParseError("Token [토큰] 형식으로 입력해주세요")