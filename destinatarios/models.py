from django.db import models

# Create your models here.
class DestinatariosModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre del Destinatario')
    rfc = models.CharField(max_length=15, verbose_name='RFC')