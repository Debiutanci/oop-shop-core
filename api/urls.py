from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r"manufacturers", views.ManufacturerViewSet, basename="manufacturers")
router.register(r"collections", views.CollectionViewSet, basename="collections")
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"orders", views.OrderViewSet, basename="orders")
router.register(r"favourities", views.FavouriteViewSet, basename="favourities")
router.register(r"carts", views.CartViewSet, basename="carts")


urlpatterns = [
	url(r"^", include(router.urls)),
]
