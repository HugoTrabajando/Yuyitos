from django.contrib import admin
from .models import Cliente, Proveedor, Producto, Abono, Venta, DetalleVenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Abono)
admin.site.register(Venta)
admin.site.register(DetalleVenta)