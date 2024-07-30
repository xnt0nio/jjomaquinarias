from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', index, name="index"),
    path('add/', login_required(add), name="add"),
    path('producto/<int:id>/', producto, name="producto"),
    path('productos/', productos, name="productos"),  
    path('contacto/', contacto, name="contacto"), 
    path('sobreNosotros/', sobreNosotros, name="sobreNosotros"),  
    path('login/', user_login, name='login'),
    path('logout/', custom_logout, name='logout'),     
    path('mensajes/', login_required(mensajes), name="mensajes"), 
    path('mision/', mision, name="mision"),  
    path('update/<int:id>/', login_required(update), name="update"), 
    path('delete/<int:id>/', login_required(delete), name="delete"), 
    path('mensaje/delete/<int:id>/', login_required(delete_mensaje), name='delete_mensaje'),  
    path('accounts/', include('django.contrib.auth.urls')),
]



urlpatterns += [
    path('<path:invalid_path>', nodisponible, name="error404"),
]
