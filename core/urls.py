from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('', index, name="index"),
    path('add/', add, name="add"),
    path('producto/<int:id>/', producto, name="producto"),
    path('productos', productos, name="productos"),
    path('contacto', contacto, name="contacto"),
    path('HistorialEmpresa', HistorialEmpresa, name="HistorialEmpresa"),
    path('vision', vision, name="vision"),
    path('mision', mision, name="mision"),

]
