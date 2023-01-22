from abc import abstractmethod

from django.db import models
from django.utils.crypto import get_random_string

from api import exceptions, oop


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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name="products")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True, related_name="products")
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, null=True, related_name="products")
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    price = models.FloatField()
    color = models.CharField(max_length=100, null=True)

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "color": oop.Color(self.color).json(),
            "category": self.category.name,
            "manufacturer": self.manufacturer.name,
            "collection": None
        }


class Order(OopShopModel):
    STATUS = [("OPE", "open"), ("CON", "confirmed"), ("COM", "completed"), ("CAN", "canceled")]

    status = models.CharField(choices=STATUS, max_length=3, default="OPE")
    price = models.FloatField()
    user = models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    comment = models.TextField(default=None, null=True)

    def display(self) -> dict:
        products = []
        for obj in self.ordered_products.all():
            products.append(obj.display())

        return {
            "identifier": self.identifier,
            "status": self.status,
            "user": self.user,
            "created": self.created,
            "last_update": self.last_update,
            "comment": self.comment,
            "products": products
        }


class OrderedProduct(OopShopModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, related_name="ordered_products")
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, related_name="ordered_products")
    single_product_price = models.FloatField()
    quantity = models.IntegerField()

    def display(self) -> dict:
        return {
            "product": self.product.name,
            "price": self.single_product_price,
            "quantity": self.quantity
        }


class Cart(OopShopModel):
    user = models.CharField(max_length=20, null=False, unique=True)

    def display(self) -> dict:
        cp = []
        for p in self.cart_products.all():
            cp.append(p.display())

        return {
            "user": self.user,
            "cart_products": cp
        }

    def clean(self):
        for relation in self.cart_products.all():
            self.remove(relation)


class CartProductRel(OopShopModel):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, null=False, related_name="cart_products")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, related_name="cart_products")
    quantity = models.IntegerField()

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "product": self.product.display()
        }


class Favourite(OopShopModel):
    user = models.CharField(max_length=20, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, related_name="favourite_users_list")

    def display(self) -> dict:
        return {
            "identifier": self.identifier,
            "user": self.user,
            "product": self.product.identifier  # TODO other info {} ?
        }
