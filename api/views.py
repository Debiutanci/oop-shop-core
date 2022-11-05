from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from api import models, serializers, exceptions, utils
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class ManufacturerViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.ManufacturerSerializer
	queryset = models.Manufacturer.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]


class CollectionViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.CollectionSerializer
	queryset = models.Collection.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]


class CategoryViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.CategorySerializer
	queryset = models.Category.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]


class ProductViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.ProductSerializer
	queryset = models.Product.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]


class OrderViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.OrderSerializer
	queryset = models.Order.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]

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
			"comment": serializer.validated_data["comment"],
			"price": serializer.validated_data["price"]
		}

		serializer = serializers.OrderSerializer(data=data)
		if not serializer.is_valid():
			raise exceptions.BadRequest(detail=serializer.errors)

		order = serializer.save()
		order.save()

		utils.assign_product_to_order(order, cart.cart_products)
		return Response(order.json(), status=status.HTTP_201_CREATED)
