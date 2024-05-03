from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from .permissions import IsSuperUser
from django.utils import timezone

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsSuperUser]

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()

        # Get all purchase orders for the vendor
        purchase_orders = vendor.purchase_orders.all()

        if not purchase_orders.exists():
            return Response({"error": "No purchase orders available for this vendor."}, status=status.HTTP_404_NOT_FOUND)

        # Calculate performance metrics
        total_orders = purchase_orders.count()
        on_time_delivery_count = purchase_orders.filter(status='completed').count()
        quality_ratings = [po.quality_rating for po in purchase_orders if po.quality_rating is not None]
        response_times = [po.response_time for po in purchase_orders if po.response_time is not None]
        fulfilled_orders_count = purchase_orders.filter(status='completed', quality_rating__isnull=False).count()


        on_time_delivery_rate = (on_time_delivery_count / total_orders) * 100 if total_orders > 0 else 0
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        average_response_time = sum(response_times) / len(response_times) if response_times else 0
        fulfillment_rate = (fulfilled_orders_count / total_orders) * 100 if total_orders > 0 else 0

        # Save historical performance data
        historical_performance = HistoricalPerformance.objects.create(
            vendor=vendor,
            date=timezone.now(),  # Assuming the current date/time
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

        # Serialize the historical performance data
        serializer = HistoricalPerformanceSerializer(historical_performance)
        return Response(serializer.data, status=status.HTTP_200_OK)
