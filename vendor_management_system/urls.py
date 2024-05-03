from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendors.views import VendorViewSet
from purchase_orders.views import PurchaseOrderViewSet

# Create a router for the APIs
router = DefaultRouter()

# Register the vendor and purchase order viewsets with the router
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
