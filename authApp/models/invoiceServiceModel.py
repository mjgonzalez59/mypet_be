from django.db import models
from .invoiceModel import Invoice
from .serviceModel import Service

class InvoiceService(models.Model):
    id = models.AutoField(primary_key=True)
    invoiceId = models.ForeignKey(Invoice, related_name='invoiceId', on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Service, related_name='serviceId', on_delete=models.CASCADE)

