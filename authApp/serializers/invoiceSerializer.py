from rest_framework import serializers
from authApp.models.invoiceModel import Invoice
from authApp.models.userModel import User
from authApp.models.invoiceServiceModel import InvoiceService
from authApp.models.serviceModel import Service

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['createdByUserId', 'paymentMethod', 'date']


    def to_representation(self, obj):
        invoiceRepresentation = Invoice.objects.get(id=obj.id)
        userRepresentation = User.objects.get(id=obj.createdByUserId.id)
        invoiceServiceRepresentation = InvoiceService.objects.filter(invoiceId_id=obj.id)
        serviceList = []

        for elem in invoiceServiceRepresentation:
            idElement = elem.serviceId_id
            serviceRepresentation = Service.objects.get(id=idElement)
            service = {}
            service["name"]= serviceRepresentation.name
            service["value"]= serviceRepresentation.value
            serviceList.append(service)

        return {
            "id": invoiceRepresentation.id,
            "createdByUserId": userRepresentation.id, 
            "paymentMethod": invoiceRepresentation.paymentMethod, 
            "date": invoiceRepresentation.date,
            "services": serviceList
        }



