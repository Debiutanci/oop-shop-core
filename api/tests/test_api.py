import pytest
from rest_framework.test import APIClient as Client
from authorization.models import User
from api import models, db
from api.tests import utils  # pylint: disable=E0401


@pytest.mark.django_db
class TestApi:
	def test_urls(self):
		c = Client()
		response = c.get("/api/")
		assert response.status_code == 200
		assert response.json() == {
			"carts": "http://testserver/api/carts/",
			"manufacturers": "http://testserver/api/manufacturers/",
			"collections": "http://testserver/api/collections/",
			"favourities": "http://testserver/api/favourities/",
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

	def test_positive_create_favourite(self, sample_database):
		sample_database()
		c = Client()
		product = models.Product.objects.all()[0].identifier

		response = c.post("/api/favourities/", data={
			"user": "user_id",
			"product": product
		})
		assert response.status_code == 201

		fav_id = models.Favourite.objects.last().identifier
		assert response.json() == {
			"identifier": fav_id,
			"user": "user_id",
			"product": product,
		}

	def test_load_db(self):
		db.default_db()
		assert models.Product.objects.count() == 7
		c = Client()
		r = c.get("/api/products/")
		assert r.status_code == 200
		assert len(r.json()) == 7

	def test_add_and_remove_to_from_cart(self, sample_database):
		sample_database()
		c = Client()
		user = User.objects.all()[0]

		p = models.Product.objects.all()[0]
		assert models.CartProductRel.objects.count() == 1
		r = c.post(f"/api/products/{p.identifier}/add-to-cart/", {
			"user": user.identifier,
		})

		assert r.status_code == 204
		assert models.CartProductRel.objects.count() == 1

		r = c.post(f"/api/products/{p.identifier}/remove-from-cart/", {
			"user": user.identifier,
		})

		assert r.status_code == 204
		assert models.CartProductRel.objects.count() == 0

		r = c.get("/api/carts/")
		assert r.status_code == 200

		r = c.post(f"/api/products/{p.identifier}/add-to-cart/", {
			"user": user.identifier,
		})

		r = c.post("/api/carts/my-cart/", {
			"user": 1
		})
		assert r.status_code == 200
		assert r.json()["cart"]["cart_products"][0]["quantity"] == 1

		r = c.post(f"/api/products/{p.identifier}/add-to-cart/", {
			"user": user.identifier,
		})

		r = c.post("/api/carts/my-cart/", {
			"user": 1
		})
		assert r.status_code == 200
		assert r.json()["cart"]["cart_products"][0]["quantity"] == 2

		instance = models.Cart.objects.all()[0]
		instance.clean()
