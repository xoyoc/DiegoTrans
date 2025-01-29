from django.db import models

# Create your models here.
class OperadoresModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    phone = models.CharField(max_length=10, verbose_name='Telefono')
