from django.db import models

# Create your models here..
class UnidadesModel(models.Model):
    num_eco= models.CharField(max_length=50, verbose_name='Numero Economico')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')

    def __str__(self):
        return f"{self.num_eco} - {self.marca} - {self.modelo}"