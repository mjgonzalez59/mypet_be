from rest_framework import status, views
from rest_framework.response import Response
from datetime import datetime

from authApp.serializers.invoiceSerializer import InvoiceSerializer
from authApp.models.serviceModel import Service
from authApp.serializers.invoiceServiceSerializer import InvoiceServiceSerializer

class InvoiceCreateView(views.APIView):
    serializer_class = InvoiceSerializer

    def post(self, request, *args, **kwargs):

        incomingData = request.data

        invoiceData = {
            "createdByUserId": incomingData['createdByUserId'], 
            "paymentMethod": incomingData['paymentMethod'], 
            "date": datetime.now(), 
        }
        
        serializer = InvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoiceInstance = serializer.save()
        invoiceId = invoiceInstance.id
        
        serviceList = []
        serviceListInput = request.data['services']
        sumValueServices = 0
        
        for service in serviceListInput:
            serviceQueryObject = Service.objects.get(id=service['serviceId'])
            serviceValue = serviceQueryObject.value

            serviceInvoiceData = {
                "invoiceId": invoiceId,
                "serviceId": service['serviceId'],
            }
            #ServiceList is being added with each service
            serviceData = {
                "name": serviceQueryObject.name, 
                "value": serviceQueryObject.value,
            }
            serviceList.append(serviceData)
            sumValueServices += serviceValue


            #Is being created invoiceService (many to many table between service and invoice) for each service from the request.data
            serializer = InvoiceServiceSerializer(data=serviceInvoiceData)
            serializer.is_valid(raise_exception=True)
            serializer.save()


        responseData = {
            "createdByUserId": invoiceData['createdByUserId'],
            "paymentMethod": invoiceData['paymentMethod'], 
            "date": invoiceData['date'], 
            "services": serviceList,
            "totalValue": sumValueServices
        }

        return Response(responseData, status=status.HTTP_201_CREATED)
        

        


# class InvoiceCreateView(views.APIView):
#     serializer_class = InvoiceSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = InvoiceSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         invoiceInstance = serializer.save()
#         invoiceId = invoiceInstance.id

#         return Response("Invoice Creado", status=status.HTTP_201_CREATED)
        

from rest_framework import generics
from authApp.models.invoiceModel import Invoice
from authApp.models.invoiceServiceModel import InvoiceService


class InvoiceDetailView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get(self, request, *args, **kwargs):

        # invoiceServicefiltered = InvoiceService.objects.filter(id=obj.id)
        # Purchase.objects.filter(purchaser__username=username)
        # InvoiceService.objects.all()
        # return Response(Invoice.objects.all(), status=status.HTTP_201_CREATED)
        return super().get(request, *args, **kwargs)
        

class InvoiceListView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        queryset = Invoice.objects.all()
        return queryset


class InvoicePerUserListView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        queryset = Invoice.objects.filter(createdByUserId=self.kwargs['user'])
        return queryset


class InvoiceUpdateView(generics.UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class InvoiceDeleteView(generics.DestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    def get(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("Invoice eliminado", status=status.HTTP_201_CREATED)
