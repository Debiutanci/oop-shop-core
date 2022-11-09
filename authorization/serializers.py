from rest_framework import serializers
from authorization import models  # noqa:


class UserSerializer(serializers.ModelSerializer):
    identifier = serializers.ReadOnlyField()
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = models.User
        fields = ["identifier", "username", "email", "name", "surname", "password"]

    def validate(self, data):  # noqa:W0221
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
