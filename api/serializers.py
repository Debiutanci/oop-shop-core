from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api import models, validators


class AbstractOopSerializer(serializers.ModelSerializer):
	identifier = serializers.CharField(read_only=True)


class ManufacturerSerializer(AbstractOopSerializer):

	class Meta:
		model = models.Manufacturer
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CollectionSerializer(AbstractOopSerializer):

	class Meta:
		model = models.Collection
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class CategorySerializer(AbstractOopSerializer):

	class Meta:
		model = models.Category
		fields = ("identifier", "name", "description")

	def validate(self, data):  # noqa:W0221
		return data


class ProductSerializer(AbstractOopSerializer):
	category = serializers.CharField(allow_null=True)
	manufacturer = serializers.CharField(allow_null=True)
	collection = serializers.CharField(allow_null=True)

	class Meta:
		model = models.Product
		fields = ("identifier", "category", "manufacturer", "collection", "name", "description", "price", "color")

	def validate(self, data):  # noqa:W0221
		#  TODO optional args implementation
		if "category" in data:
			if not models.Category.objects.filter(identifier=data["category"]).exists():
				raise ValidationError(f"Category with identifier{ data['category']} does not exist")
			data["category"] = models.Category.objects.get(identifier=data["category"])
		if "manufacturer" in data:
			if not models.Manufacturer.objects.filter(identifier=data["manufacturer"]).exists():
				raise ValidationError(f"Manufacturer with identifier{ data['manufacturer']} does not exist")
			data["manufacturer"] = models.Manufacturer.objects.get(identifier=data["manufacturer"])
		if "collection" in data:
			if not models.Collection.objects.filter(identifier=data["collection"]).exists():
				raise ValidationError(f"Collection with identifier{ data['collection']} does not exist")
			data["collection"] = models.Collection.objects.get(identifier=data["collection"])
		return data

	def to_representation(self, obj):  # noqa:W0221
		return obj.display()


class OrderCreateSerializer(AbstractOopSerializer):
	cart = serializers.CharField()

	class Meta:
		model = models.Order
		fields = ("identifier", "user", "comment", "cart")

	def validate(self, attrs):
		validators.validate_create_order(attrs)
		last_price = 0.0

		if not models.Cart.objects.filter(identifier=attrs["cart"]).exists():
			raise ValidationError(f"Cart with identifier {attrs['cart']} does not exist!")
		attrs["cart"] = models.Cart.objects.get(identifier=attrs["cart"])


		for cart_product in attrs["cart"].cart_products.all():
			last_price += cart_product.product.price
		attrs["price"] = last_price
		return attrs


class OrderSerializer(AbstractOopSerializer):
	ordered_products = serializers.ReadOnlyField()
	status = serializers.ReadOnlyField(source="get_status_display")
	created = serializers.ReadOnlyField()
	last_update = serializers.ReadOnlyField()

	class Meta:
		model = models.Order
		fields = ("identifier", "status", "price", "user", "created", "last_update", "comment", "ordered_products")

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
		data["product"] = models.Product.objects.get(identifier=data["product"])
		if not models.Order.objects.filter(identifier=data["order"]).exists():
			raise ValidationError(f"Order with identifier{data['order']} does not exist")
		data["order"] = models.Order.objects.get(identifier=data["order"])
		return data


class FavouriteSerializer(AbstractOopSerializer):
	product = serializers.CharField()

	class Meta:
		model = models.Favourite
		fields = ("identifier", "user", "product")

	def validate(self, data):  # noqa:W0221
		if not models.Product.objects.filter(identifier=data["product"]).exists():
			raise ValidationError(f"Product with identifier{data['product']} does not exist")
		data["product"] = models.Product.objects.get(identifier=data["product"])
		return data

	def to_representation(self, instance):
		return instance.display()


class AddToCartSerializer(serializers.Serializer):
	user = serializers.CharField()
	quantity = serializers.IntegerField(required=False)

	def validate(self, attrs):
		if "quantity" not in attrs:
			attrs["quantity"] = 1
		return attrs


class RemoveFromCartSerializer(serializers.Serializer):
	user = serializers.CharField()


class CartSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Cart
		fields = ("user", "cart_products")

	def to_representation(self, instance):
		return instance.display()


class GetCartSerializer(serializers.Serializer):
	user = serializers.CharField()
