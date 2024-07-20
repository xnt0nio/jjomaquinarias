from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.core.paginator import Paginator



def index(request):
    return render(request, 'core/index.html')



def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # OBTIENE LA DATA DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT INTO.....
            #data['msj'] = "Producto guardado correctamente"
            print(request, "Producto almacenado correctamente")
    return render(request, 'core/add-product.html', data)




def producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'producto': producto,
    }
    return render(request, 'core/producto.html', data)




def productos(request):
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    tipos = TipoProducto.objects.all() 

    data = {
        'listado': page_obj,
        'tipos': tipos,
    }
    return render(request, 'core/productos.html', data)



def contacto(request):
    return render(request, 'core/contacto.html')



