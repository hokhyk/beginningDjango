# encoding:utf-8
from core.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)

