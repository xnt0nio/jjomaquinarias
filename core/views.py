from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import redirect



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
    productos_similares = Producto.objects.filter(tipo=producto.tipo).exclude(id=producto.id)[:4]  
    data = {
        'producto': producto,
        'productos_similares': productos_similares,
    }
    return render(request, 'core/producto.html', data)




def productos(request):
    try:
        productos_list = Producto.objects.all()
    except Exception as e:
        print("Error al obtener productos:", e)
        productos_list = []

    paginator = Paginator(productos_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    tipos = TipoProducto.objects.all() 

    data = {
        'listado': page_obj,
        'tipos': tipos,
    }
    return render(request, 'core/productos.html', data)






def update(request, id):
    producto = Producto.objects.get(id=id) # OBTIENE UN PRODUCTO POR EL ID
    data = {
        'form' : ProductoForm(instance=producto) # CARGAMOS EL PRODUCTO EN EL FORMULARIO
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) # NUEVA INFORMACION
        if formulario.is_valid():
            formulario.save() # INSERT INTO.....
            #data['msj'] = "Producto actualizado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario # CARGA LA NUEVA INFOR EN EL FORMULARIO

    return render(request, 'core/update-product.html', data)



def delete(request, id):
    producto = get_object_or_404(Producto, id=id)  # Usa get_object_or_404 para manejar el caso en que el ID no exista
    producto.delete()
    return redirect('productos')  # Redirige a la vista de lista de productos o a cualquier otra vista





def contacto(request):
    return render(request, 'core/contacto.html')



def sobreNosotros(request):
    return render(request, 'core/sobreNosotros.html')



def contacto(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = MensajeForm()
    
    return render(request, 'core/contacto.html', {'form': form})




def vision(request):
    return render(request, 'core/vision.html')


def mision(request):
    return render(request, 'core/mision.html')



