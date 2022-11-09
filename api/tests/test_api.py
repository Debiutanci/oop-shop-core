import pytest
from rest_framework.test import APIClient as Client
from authorization.models import User
from api import models
from api.tests import utils  # pylint: disable=E0401


@pytest.mark.django_db
class TestApi:
	def test_urls(self):
		c = Client()
		response = c.get("/api/")
		assert response.status_code == 200
		assert response.json() == {
			"manufacturers": "http://testserver/api/manufacturers/",
			"collections": "http://testserver/api/collections/",
			"categories": "http://testserver/api/categories/",
			"products": "http://testserver/api/products/",
			"orders": "http://testserver/api/orders/",
		}

	def test_sample_database(self, sample_database):
		sample_database()
		assert models.Category.objects.count() == 1
		assert models.Collection.objects.count() == 1
		assert models.Manufacturer.objects.count() == 1
		assert models.Product.objects.count() == 1

	def test_positive_create_manufacturer(self):
		c = Client()

		response = c.post("/api/manufacturers/", data={
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		})
		assert response.status_code == 201
		manufacturer_identifier = models.Manufacturer.objects.last().identifier
		assert response.json() == {
			"identifier": manufacturer_identifier,
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		}

	def test_positive_create_collection(self):
		c = Client()

		response = c.post("/api/collections/", data={
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		})
		assert response.status_code == 201
		collection_identifier = models.Collection.objects.last().identifier
		assert response.json() == {
			"identifier": collection_identifier,
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		}

	def test_positive_create_category(self):
		c = Client()

		response = c.post("/api/categories/", data={
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		})
		assert response.status_code == 201
		category_identifier = models.Category.objects.last().identifier
		assert response.json() == {
			"identifier": category_identifier,
			"name": "ikypgborezsubwdpqiqs",
			"description": "bfxmhbqaxhkkvrmxnfnf",
		}

	def test_create_order(self, sample_database):
		c = Client()
		sample_database()

		cart = models.Cart.objects.all()[0]
		user = User.objects.all()[0]

		r = c.post("/api/orders/", {
			"user": user.identifier,
			"cart": cart.identifier
		})

		assert r.status_code == 201
		order = models.Order.objects.last()
		assert r.json() == {
            "identifier": order.identifier,
            "status": "OPE",
            "user": str(user.identifier),
            "created": utils.date_format(order.created),
            "last_update": utils.date_format(order.last_update),
            "comment": None,
            "products": [{'price': 20.2, 'product': 'pianino', 'quantity': 2}]
        }
