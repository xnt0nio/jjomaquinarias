from django.contrib import admin
from .models import TipoProducto, Producto 

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'descripcion', 'tipo', 'vigente']
    search_fields = ['nombre', 'descripcion', 'marca', 'modelo']  
    list_per_page = 10  
    list_filter = ['tipo', 'vigente']  
    list_editable = ['stock', 'descripcion', 'tipo', 'vigente']  

# Registra los modelos en el administrador de Django
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)