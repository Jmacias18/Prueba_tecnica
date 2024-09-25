from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()


    nombre = request.GET.get('nombre')
    grupo = request.GET.get('grupo')
    familia = request.GET.get('familia')

    if nombre:
        productos = productos.filter(nombre_producto__icontains=nombre)
    if grupo:
        productos = productos.filter(id_grupo__nombre_grupo__icontains=grupo)
    if familia:
        productos = productos.filter(id_familia__nombre_familia__icontains=familia)

    paginator = Paginator(productos, 10)  # Mostrar 10 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'aplicacion1/producto_list.html', {'page_obj': page_obj})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'aplicacion1/producto_detail.html', {'producto': producto})

def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'aplicacion1/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'aplicacion1/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'aplicacion1/producto_confirm_delete.html', {'producto': producto})