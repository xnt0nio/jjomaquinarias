from django.contrib import admin
from .models import TipoProducto, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'tipo', 'marca', 'modelo', 'motor', 'potencia', 'traccion', 'alimentacion', 'neumaticos', 'caracteristica', 'vigente']
    search_fields = ['nombre', 'descripcion', 'marca', 'modelo']
    list_per_page = 10
    list_filter = ['tipo', 'vigente']
    list_editable = ['descripcion', 'tipo', 'vigente', 'marca', 'modelo', 'motor', 'potencia', 'traccion', 'alimentacion', 'neumaticos', 'caracteristica']

# Registra los modelos en el administrador de Django
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
