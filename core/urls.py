from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', index, name="index"),
    path('add/', login_required(add), name="add"),
    path('producto/<int:id>/', producto, name="producto"),
    path('productos/', productos, name="productos"),  # Agregado '/' al final
    path('contacto/', contacto, name="contacto"),  # Agregado '/' al final
    path('sobreNosotros/', sobreNosotros, name="sobreNosotros"),  # Agregado '/' al final
    path('login/', user_login, name='login'),
    
    path('mensajes/', login_required(mensajes), name="mensajes"),  # Agregado '/' al final y login_required
    path('mision/', mision, name="mision"),  # Agregado '/' al final
    path('update/<int:id>/', login_required(update), name="update"),  # Añadido login_required y corregido el tipo de parámetro
    path('delete/<int:id>/', login_required(delete), name="delete"),  # Añadido login_required y corregido el tipo de parámetro
    path('mensaje/delete/<int:id>/', login_required(delete_mensaje), name='delete_mensaje'),  # Añadido login_required
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('<path:invalid_path>', nodisponible, name="error404"),
]
