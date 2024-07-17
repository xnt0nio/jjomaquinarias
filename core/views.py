from django.shortcuts import render
from .forms import *
from .models import *


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




def productos(request):
   
    productosAll = Producto.objects.all()

   


    data = {
        'listado': productosAll,
      
    }
    return render(request, 'core/productos.html',data)
