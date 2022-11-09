from rest_framework.exceptions import ValidationError
from authorization.models import User


def validate_create_order(attrs):
    if not User.objects.filter(identifier=attrs["user"]).exists():
        raise ValidationError("User not in db")
