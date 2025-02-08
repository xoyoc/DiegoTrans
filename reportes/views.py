from django.shortcuts import render
import datetime
import csv

from transporte.semanas import obtener_semanas_del_año
from .models import ReporteModel
from registros.models import RegistrosModel

# Create your views here.
def crear_ano_semana(request):
    ano_presente = datetime.datetime.now().year
    semanas = obtener_semanas_del_año(ano_presente)
    for i, (inicio, fin) in enumerate(semanas, start=1):
        obj = ReporteModel.objects.create(
            numero_semana = int(i),
            inicio_semana = inicio,
            fin_semana = fin
        )
        obj.save()
    return render(request, 'base.html')

def estadisticas(request):
    semanas=[]
    totales=[]
    dict = {}
    reportes = ReporteModel.objects.all()
    for reporte in reportes:
        semanas.append(reporte.numero_semana)
        totales.append(reporte.total)
    context = {
        'semanas': semanas,
        'totales':totales,
    }

    for semanas, totales in zip(semanas, totales):
        keys = str(semanas)
        dict.setdefault(keys, totales)
    
    dict = [
                {'Semana': 1,'Totales':0.00,}, 
                {'Semana': 2,'Totales':0.00,}, 
                {'Semana': 3,'Totales':0.00,}, 
                {'Semana': 4,'Totales':0.00,}, 
                {'Semana': 5,'Totales':146180.08,}, 
                {'Semana': 6,'Totales':0.00,}
            ]
    
    with open('estadisticas.csv', mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=['Semana', 'Totales'])
        writer.writeheader()
        for row in dict:
            writer.writerow(row)
    print(dict)
    print(type(dict))
    return render(request, 'base.html', context)

def semanas(request):
    reportes = ReporteModel.objects.all()
    registros = RegistrosModel.objects.all()
    cantidad_registros = 0
    totales = float()
    for reporte in reportes:
        semana = reporte.numero_semana
        obj = ReporteModel.objects.get(id = reporte.id)
        if reporte.is_complete == False:
            for registro in registros:
                fecha = registro.date
                num_sem = int(fecha.strftime('%V'))
                if semana == num_sem:
                    cantidad_registros += 1
                    totales += float(registro.total)
                    print(f'la semana {semana} es igual a {num_sem}')
                    obj.is_complete = True
                    obj.cantidad_registros = cantidad_registros
                    obj.total = round(totales,2)
                    obj.save()
        cantidad_registros = 0
        totales = 0.00 
    context = {
        'cantidad_registros': cantidad_registros,
        'totales':totales
    }
    return render(request, 'base.html', context)

def semanas_false(request):
    reportes = ReporteModel.objects.all()
    for reporte in reportes:
        obj = ReporteModel.objects.get(id = reporte.id)
        obj.is_complete = False
        obj.save()
    context = {}
    return render(request, 'base.html', context)