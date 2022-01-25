from rest_framework import serializers
from authApp.models.invoiceServiceModel import InvoiceService

class InvoiceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceService
        fields = ['invoiceId', 'serviceId']


