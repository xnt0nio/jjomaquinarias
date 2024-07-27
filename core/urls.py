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
    path('sobreNosotros', sobreNosotros, name="sobreNosotros"),
    path('mensajes', mensajes, name="mensajes"),
    path('mision', mision, name="mision"),
    path('contacto/', contacto, name='contacto'),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    
    path('mensaje/delete/<int:id>/', delete_mensaje, name='delete_mensaje'),

]
