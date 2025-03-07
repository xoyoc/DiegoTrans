# Generated by Django 5.1.5 on 2025-01-29 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('destinatarios', '0002_destinatariosmodel_destino'),
        ('operadores', '0001_initial'),
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('imp_exp', models.CharField(choices=[('IMP', 'IMP'), ('EXP', 'EXP')], max_length=3, verbose_name='IMP/EXP')),
                ('bl_bk', models.CharField(max_length=100, verbose_name='BL/BK')),
                ('order_w', models.CharField(max_length=100, verbose_name='Work Order')),
                ('container', models.CharField(max_length=11, verbose_name='Contenedor')),
                ('tipo_c', models.CharField(max_length=4, verbose_name='Tipo Cont.')),
                ('date_posc_pta', models.DateField(verbose_name='Fecha Posc. Pta.')),
                ('mod', models.IntegerField(verbose_name='Mod.')),
                ('cpc', models.CharField(max_length=10, verbose_name='C.P.C.')),
                ('statement_id', models.CharField(max_length=50, verbose_name='Statement ID')),
                ('factura', models.CharField(max_length=50, verbose_name='Factura')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='SubTotal')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='I.V.A.')),
                ('ret_iva', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ret. I.V.A.')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total')),
                ('clienteid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.clientesmodel', verbose_name='Cliente')),
                ('destinatariosid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destinatarios.destinatariosmodel', verbose_name='Destinatario')),
                ('operadorid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='operadores.operadoresmodel', verbose_name='Operador')),
                ('unidadid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unidades.unidadesmodel', verbose_name='Unidad')),
            ],
        ),
    ]
