from rest_framework import serializers
from .models import Vendor, HistoricalPerformance

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ['id', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
        read_only_fields = ['id', 'date']

class VendorSerializer(serializers.ModelSerializer):
    historical_performance = HistoricalPerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code', 'historical_performance']
        read_only_fields = ['vendor_code']
