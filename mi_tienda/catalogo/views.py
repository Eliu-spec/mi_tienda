from django.shortcuts import render, get_object_or_404
from .models import Product

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def lista_productos(request):
    productos = Product.objects.filter(disponible=True)
    return render(request, 'catalogo/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    return render(request, 'catalogo/detalle_producto.html', {'producto': producto})