from api import models, validators
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ManufacturerSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)

	class Meta:
		model = models.Manufacturer
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CollectionSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)

	class Meta:
		model = models.Collection
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CategorySerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)

	class Meta:
		model = models.Category
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class ProductSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)
	category = serializers.CharField()
	manufacturer = serializers.CharField()
	collection = serializers.CharField()

	class Meta:
		model = models.Product
		fields = ("identifier", "category", "manufacturer", "collection", "name", "description", "price", "color")

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


class OrderCreateSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)
	status = serializers.ReadOnlyField(source="get_status_display")
	cart = serializers.CharField()

	class Meta:
		model = models.Order
		fields = ("user", "comment", "cart")

	def validate(self, attrs):
		validators.validate_create_order(attrs)
		last_price = 0.0
		for cart_product in attrs["cart"].cart_products.all():
			last_price += cart_product.product.price
		attrs["price"] = last_price
		return attrs


class OrderSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)
	ordered_products = serializers.ReadOnlyField()
	status = serializers.ReadOnlyField(source="get_status_display")
	created = serializers.ReadOnlyField()
	last_update = serializers.ReadOnlyField()

	class Meta:
		model = models.Order
		fields = ("status", "price", "user", "created", "last_update", "comment", "ordered_products")

	def validate(self, data):  # noqa:W0221
		return data


class OrderedProductSerializer(serializers.ModelSerializer):
	product = serializers.CharField()
	order = serializers.CharField()

	class Meta:
		model = models.OrderedProduct
		fields = ("product", "order", "price", "quantity")

	def validate(self, data):  # noqa:W0221
		if not models.Product.objects.filter(identifier=data["product"]).exists():
			raise ValidationError(f"Product with identifier{data['product']} does not exist")
		data["product"] = models.Product.objects.get(product=data["product"])
		if not models.Order.objects.filter(identifier=data["order"]).exists():
			raise ValidationError(f"Order with identifier{data['order']} does not exist")
		data["order"] = models.Order.objects.get(order=data["order"])
		return data
