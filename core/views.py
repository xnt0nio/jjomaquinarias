from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'core/index.html')



@login_required
def add(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            print(request, "Producto almacenado correctamente")
    return render(request, 'core/add-product.html', data)




def sobreNosotros(request):
    return render(request, 'core/sobreNosotros.html')




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


@login_required
def update(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario

    return render(request, 'core/update-product.html', data)


@login_required
def delete(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('productos')


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


@login_required
def mensajes(request):
    mensajes = mensaje.objects.all().order_by('-fecha')
    return render(request, 'core/mensajes.html', {'mensajes': mensajes})


@login_required
def delete_mensaje(request, id):
    mensaje_instance = get_object_or_404(mensaje, id=id)
    mensaje_instance.delete()
    return redirect('mensajes')


def nodisponible(request, invalid_path=None):
    return render(request, 'core/nodisponible.html')


def mision(request):
    return render(request, 'core/mision.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {username}!")
                return redirect('index')  # Redirige a la página de inicio o a la que desees
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

from django.contrib.auth import logout

def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')  # Redirige a la página de inicio o a la que desees
    else:
        return redirect('index')