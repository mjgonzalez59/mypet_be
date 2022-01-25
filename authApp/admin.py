from django.contrib import admin
from .models.userModel import User
from .models.invoiceModel import Invoice
from .models.serviceModel import Service
# from .models.invoiceServiceModel import InvoiceService

# Register your models here.
admin.site.register(User)
admin.site.register(Invoice)
admin.site.register(Service)
# admin.site.register(InvoiceService)
