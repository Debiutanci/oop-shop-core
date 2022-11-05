import pytest
from rest_framework.test import APIClient as Client
from django.db import models


@pytest.mark.django_db
class TestApi:
	def test_urls(self):
		c = Client()
		response = c.get("http://testserver/api_oop/")
		assert response.status_code == 200
		assert response.json() == {
			"users": "http://testserver/api_oop/users/",
			"manufacturers": "http://testserver/api_oop/manufacturers/",
			"collections": "http://testserver/api_oop/collections/",
			"categories": "http://testserver/api_oop/categories/",
			"products": "http://testserver/api_oop/products/",
			"orders": "http://testserver/api_oop/orders/",
			"orderedproducts": "http://testserver/api_oop/orderedproducts/",
		}

	def test_positive_create_models(self):
		c = Client()
		response = c.post("http://testserver/api_oop/user/", data={
			"name": "rpbmuycxkhyzvdyftkmk",
			"surname": "jocutbjsnexeczzwjfzi",
			"email": "nvhhawimnhrwmiriyykb",
			"age": 35,
		})

		assert response.status_code == 201

		user_identifier = models.User.objects.last().identifier
		assert response.json() == {
			"identifier": user_identifier,
			"name": "rpbmuycxkhyzvdyftkmk",
			"surname": "jocutbjsnexeczzwjfzi",
			"email": "nvhhawimnhrwmiriyykb",
			"age": 35,
		}

		response = c.post("http://testserver/api_oop/manufacturer/", data={
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

		response = c.post("http://testserver/api_oop/collection/", data={
			"name": "myqlmmlqshborrnxnmdy",
			"description": "klwanijdjjxpzytmxegy",
		})

		assert response.status_code == 201

		collection_identifier = models.Collection.objects.last().identifier
		assert response.json() == {
			"identifier": collection_identifier,
			"name": "myqlmmlqshborrnxnmdy",
			"description": "klwanijdjjxpzytmxegy",
		}

		response = c.post("http://testserver/api_oop/category/", data={
			"name": "qtuljgcmzpmhvnrtkqov",
			"description": "arjmwibzntbkjxdpophs",
		})

		assert response.status_code == 201

		category_identifier = models.Category.objects.last().identifier
		assert response.json() == {
			"identifier": category_identifier,
			"name": "qtuljgcmzpmhvnrtkqov",
			"description": "arjmwibzntbkjxdpophs",
		}

		response = c.post("http://testserver/api_oop/product/", data={
			"category": category_identifier,
			"manufacturer": manufacturer_identifier,
			"collection": collection_identifier,
			"name": "aqsnnwllstwagezcoozq",
			"description": "bvxtkxmtujerkfqnlirz",
			"price": "rpxqhhctublmfqdvjwyw",
			"color": "wilfqkrwdrvwnikokndg",
		})

		assert response.status_code == 201

		product_identifier = models.Product.objects.last().identifier
		assert response.json() == {
			"identifier": product_identifier,
			"category": category_identifier,
			"manufacturer": manufacturer_identifier,
			"collection": collection_identifier,
			"name": "aqsnnwllstwagezcoozq",
			"description": "bvxtkxmtujerkfqnlirz",
			"price": "rpxqhhctublmfqdvjwyw",
			"color": "wilfqkrwdrvwnikokndg",
		}

		response = c.post("http://testserver/api_oop/order/", data={
			"name": "ztgtegpkeoeixzkbqhav",
			"user": user_identifier,
			"date": "vpnaqtlhhxouupqqcnjq",
		})

		assert response.status_code == 201

		order_identifier = models.Order.objects.last().identifier
		assert response.json() == {
			"identifier": order_identifier,
			"name": "ztgtegpkeoeixzkbqhav",
			"user": user_identifier,
			"date": "vpnaqtlhhxouupqqcnjq",
		}

		response = c.post("http://testserver/api_oop/orderedproduct/", data={
			"product": product_identifier,
			"order": order_identifier,
			"price": "hoppchoiezchcdkdqxrr",
			"quantity": "rddvgxrpyibjrdiejfgd",
		})

		assert response.status_code == 201

		orderedproduct_identifier = models.OrderedProduct.objects.last().identifier
		assert response.json() == {
			"identifier": orderedproduct_identifier,
			"product": product_identifier,
			"order": order_identifier,
			"price": "hoppchoiezchcdkdqxrr",
			"quantity": "rddvgxrpyibjrdiejfgd",
		}

