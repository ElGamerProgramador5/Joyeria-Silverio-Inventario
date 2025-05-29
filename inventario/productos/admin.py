from django.contrib import admin
from .models import Producto, Material

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'material', 'existencias', 'precio_compra', 'precio_venta')
    search_fields = ('id',)

admin.site.register(Material)
