from rest_framework import permissions
from rest_framework.authtoken.models import Token


class CustomReadOnly(permissions.BasePermission):
    # Sample Code
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     header_token = request.headers['Authorization'].split(' ')[1]
    #     target_token = Token.objects.get(user=obj.user)
    #
    #     return header_token == target_token

    pass
