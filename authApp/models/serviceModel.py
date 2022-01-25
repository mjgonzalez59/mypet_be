from django.db import models

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, default=0)
    value = models.FloatField(default=0)
