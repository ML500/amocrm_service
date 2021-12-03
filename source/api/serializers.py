from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    grant_type = serializers.CharField(max_length=30)
    refresh_token = serializers.CharField(max_length=255, required=False)
