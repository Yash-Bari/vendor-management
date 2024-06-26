from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'purchase_orders', PurchaseOrderViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
