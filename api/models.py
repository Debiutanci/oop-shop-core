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

class Manufacturer(models.Model):
	identifier = models.CharField(max_length=100, null=False)
	name = models.CharField(max_length=100, null=False)
	description = models.CharField(max_length=100, null=False)


class Collection(models.Model):
	identifier = models.CharField(max_length=100, null=False)
	name = models.CharField(max_length=100, null=False)
	description = models.CharField(max_length=100, null=True)


class Category(models.Model):
	identifier = models.CharField(max_length=100, null=False)
	name = models.CharField(max_length=100, null=False)
	description = models.CharField(max_length=100, null=True)


class Product(models.Model):
	identifier = models.CharField(max_length=100, null=False)
	category = models.ForeignKey(null=False)
	manufacturer = models.ForeignKey(null=False)
	collection = models.ForeignKey(null=False)
	name = models.CharField(max_length=100, null=False)
	description = models.CharField(max_length=100, null=False)
	price = models.CharField(max_length=100, null=False)
	color = models.CharField(max_length=100, null=False)


class Order(models.Model):
	name = models.CharField(max_length=100, null=False)
	user = models.ForeignKey(null=False)
	date = models.CharField(max_length=100, null=False)


class OrderedProduct(models.Model):
	product = models.ForeignKey(null=False)
	order = models.ForeignKey(null=False)
	price = models.CharField(max_length=100, null=False)
	quantity = models.CharField(max_length=100, null=False)
