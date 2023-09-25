from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=9,null=True)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=50)
    correo_cliente = models.CharField(max_length=50,null=True)

    def __str__(self):
        return "rut "+self.rut_cliente+" - nombre "+self.nombre_cliente+" "+self.apellido_cliente
    
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut_proveedor = models.CharField(max_length=9,null=True)
    nombre_proveedor = models.CharField(max_length=50)
    apellido_proveedor = models.CharField(max_length=50)
    direccion_proveedor = models.CharField(max_length=50,null=True)
    telefono_proveedor = models.CharField(max_length=50,null=True)
    correo_proveedor = models.CharField(max_length=50,null=True)

    def __str__(self):
        return "rut "+self.rut_proveedor+" - nombre "+self.nombre_proveedor+" "+self.apellido_proveedor
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    marca = models.CharField(max_length=40)
    existencia_actual = models.BooleanField(default=False)
    codigo_familia = models.IntegerField()
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return f"id producto: {str(self.id_producto)} - descr: {self.descripcion} - codigo familia: {str(self.codigo_familia)}"
    
class Abono(models.Model):
    numero_boleta = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=9)
    fecha_transaccion = models.CharField(max_length=19,null=True)
    monto_compra = models.IntegerField()
    estado = models.CharField(
        max_length=10,
        choices=[('CANCELADA', 'CANCELADA'), ('PENDIENTE', 'PENDIENTE')],
        default='PENDIENTE'
    )

    def __str__(self):
        return f'Boleta {str(self.numero_boleta)} - Cliente: {self.rut_cliente}'

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.CharField(max_length=19,null=True)
    productos_vendidos = models.ManyToManyField(Producto, through='DetalleVenta')
    total_venta = models.IntegerField()
    es_credito = models.BooleanField(default=False)

    def __str__(self):
        return f'Boleta de Venta #{str(self.id_venta)} - Fecha: {self.fecha_venta}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de Venta #{self.venta.id} - Producto: {self.producto.nombre}'