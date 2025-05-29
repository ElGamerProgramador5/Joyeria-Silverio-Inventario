from django.shortcuts import render
from .models import Producto, Material

def panel_inventario(request):
    productos = Producto.objects.all()
    materiales = Material.objects.values_list('nombre', flat=True)

    id_query = request.GET.get('id')
    material_query = request.GET.get('material')

    if id_query:
        productos = productos.filter(id=id_query)

    if material_query and material_query != 'Todos':
        productos = productos.filter(material__nombre=material_query)

    return render(request, 'productos/panel.html', {
        'productos': productos,
        'materiales': materiales
    })
