from django.db import models
from .userModel import User
from datetime import datetime

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    createdByUserId = models.ForeignKey(User, related_name='invoiceCreatedByUserId', on_delete=models.CASCADE)
    paymentMethod = models.CharField('PaymentMethod', max_length=100, default=0)
    date = models.DateTimeField(default=datetime.now)

