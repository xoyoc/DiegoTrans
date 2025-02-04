from django.db import models

# Create your models here.
class ClientesModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre del Cliente')
    rfc = models.CharField(max_length=15, verbose_name='RFC')

    def __str__(self):
        return f"{self.name} - {self.rfc}"