from django.db import models
from abc import abstractmethod
from django.utils.crypto import get_random_string
from api import exceptions


def random_string_length_20():
    return get_random_string(length=20)


class OopShopModel(models.Model):
    identifier = models.CharField(max_length=20, default=random_string_length_20)

    class Meta:
        abstract = True

    @abstractmethod
    def display(self) -> dict:
        raise exceptions.MustBeOverWrittenException()


class BaseOopShopModel(OopShopModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()

    class Meta:
        abstract = True

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "name": self.name,
            "description": self.description
        }


class Manufacturer(BaseOopShopModel):
    pass


class Collection(BaseOopShopModel):
    pass


class Category(BaseOopShopModel):
    pass


class Product(OopShopModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    price = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "name": self.name,
            "description": self.description
        }


class Order(OopShopModel):
    STATUS = [("OPE", "open"), ("CON", "confirmed"), ("COM", "completed"), ("CAN", "canceled")]

    status = models.CharField(choices=STATUS, max_length=3, default="OPE")
    user = models.CharField(max_length=20, null=False)
    date = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    comment = models.TextField(default=None, null=True)

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "status": self.status,
            "user": self.user,
            "date": self.date,
            "created": self.created,
            "last_update": self.last_update,
            "comment": self.comment
        }


class OrderedProduct(OopShopModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=False)
    price = models.FloatField()
    quantity = models.IntegerField()

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "product": self.product.name,
            "price": self.price,
            "quantity": self.quantity
        }
