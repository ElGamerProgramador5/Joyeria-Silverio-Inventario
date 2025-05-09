from django.shortcuts import render
from .models import Producto

def panel_control(request):
    productos = Producto.objects.all()
    material_filter = request.GET.get('material')
    query = request.GET.get('q')

    if material_filter and material_filter != 'Todos':
        productos = productos.filter(material__icontains=material_filter)

    if query:
        productos = productos.filter(nombre__icontains=query)

    materiales = Producto.objects.values_list('material', flat=True).distinct()

    return render(request, 'productos/panel.html', {
        'productos': productos,
        'materiales': materiales,
    })
