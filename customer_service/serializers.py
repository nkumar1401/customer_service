from rest_framework import serializers
from .models import *


class ServiceRequestSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.username", read_only=True)

    class Meta:
        model = ServiceRequest
        fields = ['id', 'customer', 'customer_name', 'service_type', 'description', 'attachment', 'status', 'created_at', 'updated_at']
        read_only_fields = ['customer', 'status', 'created_at', 'updated_at']
