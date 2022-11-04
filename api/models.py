from django.db import models
from abc import abstractmethod
from django.utils.crypto import get_random_string


def random_string_length_20():
    return get_random_string(length=20)
# Create your models here.

class OopShopModel(models.Model):
    identifier = models.CharField(max_length=20, default=random_string_length_20)

    @abstractmethod
    def display(self):
        ...


class BaseOopShopModel(OopShopModel):
    name = ...
    description = ...


class Product(OopShopModel):
    PRODUCT_TYPES = [("I", "instrument"), ("A", "accessory"), ("", ""), ("", "")]

    name = ...

    def display():
        ...