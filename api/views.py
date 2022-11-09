from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.response import Response

from api import models, serializers, exceptions, utils


class ManufacturerViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.ManufacturerSerializer
	queryset = models.Manufacturer.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]


class CollectionViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.CollectionSerializer
	queryset = models.Collection.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]


class CategoryViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.CategorySerializer
	queryset = models.Category.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]


class ProductViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.ProductSerializer
	queryset = models.Product.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]


class OrderViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.OrderSerializer
	queryset = models.Order.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]

	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ["user"]
	ordering_fields = ["user"]

	def get_serializer_class(self):
		if self.action in ["create"]:
			return serializers.OrderCreateSerializer
		return serializers.OrderSerializer

	def get_queryset(self, *args, **kwargs):
		qs = super().get_queryset(*args, **kwargs)
		if "search" not in self.request.GET:
			qs.order_by("+name")
		return qs

	def create(self, request, *args, **kwargs):  # noqa:W0221
		# TODO auth part
		# if not request.user:
		# 	raise PermissionDenied(detail="You must be log in!")

		serializer_class = self.get_serializer_class()
		serializer = serializer_class(data=request.data)
		if not serializer.is_valid():
			raise exceptions.BadRequest(detail=serializer.errors)

		cart = serializer.validated_data["cart"]

		data = {
			"user": serializer.validated_data["user"],
			"price": serializer.validated_data["price"]
		}
		if "comment" in serializer.validated_data:
			data["comment"] = serializer.validated_data["comment"]

		serializer = serializers.OrderSerializer(data=data)
		if not serializer.is_valid():
			raise exceptions.BadRequest(detail=serializer.errors)

		order = serializer.save()
		order.save()

		utils.assign_product_to_order(order, cart.cart_products)
		return Response(order.display(), status=status.HTTP_201_CREATED)


class FavouriteViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.FavouriteSerializer
	queryset = models.Favourite.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["post", "get", "put"]