from api_oop import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.User
		fields = ("id", "identifier", "name", "surname", "email", "age")

	def validate(self, data):  # noqa:W0221
		data["name"] = data["name"].strip()
		return data


class ManufacturerSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Manufacturer
		fields = ("id", "identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CollectionSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Collection
		fields = ("id", "identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CategorySerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Category
		fields = ("id", "identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class ProductSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	category = serializers.CharField()
	manufacturer = serializers.CharField()
	collection = serializers.CharField()

	class Meta:
		model = models.Product
		fields = ("id", "identifier", "category", "manufacturer", "collection", "name", "description", "price", "color")

	def validate(self, data):  # noqa:W0221
		if not models.Category.objects.filter(identifier=data["category"]).exists():
			raise ValidationError(f"Category with identifier{ data['category']} does not exist")
		data["category"] = models.Category.objects.get(category=data["category"])
		if not models.Manufacturer.objects.filter(identifier=data["manufacturer"]).exists():
			raise ValidationError(f"Manufacturer with identifier{ data['manufacturer']} does not exist")
		data["manufacturer"] = models.Manufacturer.objects.get(manufacturer=data["manufacturer"])
		if not models.Collection.objects.filter(identifier=data["collection"]).exists():
			raise ValidationError(f"Collection with identifier{ data['collection']} does not exist")
		data["collection"] = models.Collection.objects.get(collection=data["collection"])
		return data


class OrderSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	user = serializers.CharField()

	class Meta:
		model = models.Order
		fields = ("id", "name", "user", "date")

	def validate(self, data):  # noqa:W0221
		if not models.User.objects.filter(identifier=data["user"]).exists():
			raise ValidationError(f"User with identifier{ data['user']} does not exist")
		data["user"] = models.User.objects.get(user=data["user"])
		return data


class OrderedProductSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	product = serializers.CharField()
	order = serializers.CharField()

	class Meta:
		model = models.OrderedProduct
		fields = ("id", "product", "order", "price", "quantity")

	def validate(self, data):  # noqa:W0221
		if not models.Product.objects.filter(identifier=data["product"]).exists():
			raise ValidationError(f"Product with identifier{ data['product']} does not exist")
		data["product"] = models.Product.objects.get(product=data["product"])
		if not models.Order.objects.filter(identifier=data["order"]).exists():
			raise ValidationError(f"Order with identifier{ data['order']} does not exist")
		data["order"] = models.Order.objects.get(order=data["order"])
		return data
