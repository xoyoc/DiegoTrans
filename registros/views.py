from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import RegistrosModel

# Create your views here.

class CrearRegistrosView(CreateView):
    model = RegistrosModel
    fields = '__all__'
    template_name = 'registros/CreateRegistros.html'
    success_url = reverse_lazy('lista_registros')

class EditRegistrosView(UpdateView):
    ...

class EliminarRegistrosView(DeleteView):
    ...

class ListaRegistrosView(ListView):
    model = RegistrosModel
    fields = '__all__'
    context_object_name = 'list_registros'
    template_name = 'registros/ListaRegistros.html'