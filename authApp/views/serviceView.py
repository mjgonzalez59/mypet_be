from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.serviceSerializer import ServiceSerializer

class ServiceCreateView(views.APIView):
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Service Creado", status=status.HTTP_201_CREATED)


from rest_framework import generics
from authApp.models.serviceModel import Service

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    def get_queryset(self):
        queryset = Service.objects.all()
        return queryset



class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    def get(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("Service eliminado", status=status.HTTP_201_CREATED)
