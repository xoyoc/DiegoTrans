"""
URL configuration for transporte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import home
from registros.views import CrearRegistrosView, ListaRegistrosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('registros/crear', CrearRegistrosView.as_view(), name='crear_registro'),
    path('registros/lista', ListaRegistrosView.as_view(), name='lista_registros'),
]
