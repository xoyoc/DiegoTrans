from django.db import models

# Create your models here.
class ReporteModel(models.Model):
    numero_semana = models.IntegerField()
    inicio_semana = models.DateField()
    fin_semana = models.DateField()
    cantidad_registro = models.IntegerField(null=True,blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=9,null=True,blank=True)
    is_complete = models.BooleanField(default=False)

