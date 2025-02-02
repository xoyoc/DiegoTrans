from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import RegistrosModel

# Create your views here.

class CrearRegistrosView(CreateView):
    model = RegistrosModel
    fields = '__all__'
    template_name = 'registros/CreateRegistros.html'

class EditRegistrosView(UpdateView):
    ...

class EliminarRegistrosView(DeleteView):
    ...

class ListaRegistrosView(ListView):
    model = RegistrosModel
    fields = '__all__'
    template_name = 'registros/ListaRegistros.html'