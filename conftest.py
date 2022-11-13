import pytest
import django

# from jose import jwt
from django.conf import settings
from rest_framework.test import APIClient as Client
from api import models
from authorization.models import User


def pytest_configure():
    # config vars
    settings.PROJECT = "oop-shop-core"

    # config database
    # TODO ??
    django.setup()


@pytest.fixture
def client():
    def factory(uid=None, roles=None):  # noqa
        return Client()

    return factory


@pytest.fixture(scope="function")
def sample_database():
    def db():
        user = User.objects.create(
            username="some_username",
            name="jan",
            surname="kowalski",
            email="jan.kowalski@test.pl",
            password="test1234"
        )
        identifier = user.identifier

        category = models.Category.objects.create(name="category1", description="cat_des_1")
        manufacturer = models.Manufacturer.objects.create(name="manufacturer1", description="man_des_1")
        collection = models.Collection.objects.create(name="collection1", description="col_des_1")

        product = models.Product.objects.create(
            category=category,
            manufacturer=manufacturer,
            collection=collection,
            name="pianino",
            description="abc",
            price=20.20,
            color="czerwony"
        )

        cart = models.Cart.objects.create(user=identifier)
        models.CartProductRel.objects.create(
            cart=cart,
            product=product,
            quantity=2
        )

    return db
