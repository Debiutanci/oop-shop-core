from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from api_oop import models, serializers


class UserViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.UserSerializer
	queryset = models.User.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]


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

	def get_queryset(self, *args, **kwargs):
		qs = super().get_queryset(*args, **kwargs)
		if "search" not in self.request.GET:
			qs.order_by("+name")
		return qs


class OrderedProductViewSet(ModelViewSet):  # pylint: disable=R0901
	serializer_class = serializers.OrderedProductSerializer
	queryset = models.OrderedProduct.objects.all()
	lookup_field = "identifier"
	lookup_url_kwarg = "identifier"
	http_method_names = ["create", "update", "retrieve", "list"]
