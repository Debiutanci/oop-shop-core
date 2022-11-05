import pytest
from rest_framework.test import APIClient as Client
from api import models


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
