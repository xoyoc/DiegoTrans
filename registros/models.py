from django.db import models

from clientes.models import ClientesModel
from destinatarios.models import DestinatariosModel
from operadores.models import OperadoresModel
from unidades.models import UnidadesModel

# Create your models here.
class RegistrosModel(models.Model):
    date = models.DateField(auto_now=True, verbose_name='Fecha')
    clienteid = models.ForeignKey(ClientesModel, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    destinatariosid = models.ForeignKey(DestinatariosModel, on_delete=models.DO_NOTHING, verbose_name='Destinatario')
    unidadid = models.ForeignKey(UnidadesModel, on_delete=models.DO_NOTHING, verbose_name='Unidad')
    operadorid = models.ForeignKey(OperadoresModel, on_delete=models.DO_NOTHING, verbose_name='Operador')
    imp_exp = models.CharField(choices={'IMP':'IMP','EXP':'EXP'}, max_length=3, verbose_name='IMP/EXP')
    bl_bk = models.CharField(max_length=100, verbose_name='BL/BK')
    order_w = models.CharField(max_length=100, verbose_name='Work Order')
    container = models.CharField(max_length=11, verbose_name='Contenedor')
    tipo_c = models.CharField(max_length=4, verbose_name='Tipo Cont.')
    date_posc_pta = models.DateField(verbose_name='Fecha Posc. Pta.')
    mod = models.IntegerField(verbose_name='Mod.')
    cpc = models.CharField(max_length=10, verbose_name='C.P.C.')
    statement_id = models.CharField(max_length=50, verbose_name='Statement ID')
    factura = models.CharField(max_length=50, verbose_name='Factura')
    subtotal = models.DecimalField(decimal_places=2,max_digits=8, verbose_name='SubTotal')
    iva = models.DecimalField(decimal_places=2,max_digits=8, verbose_name='I.V.A.')
    ret_iva = models.DecimalField(decimal_places=2,max_digits=8, verbose_name='Ret. I.V.A.')
    total = models.DecimalField(decimal_places=2,max_digits=8, verbose_name='Total')

  
