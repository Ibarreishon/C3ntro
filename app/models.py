from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha',)


class Producto(models.Model):
    """
    Modelo de Producto con los campos solicitados en el documento
    """
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='productos', null=True)

    class Meta:
        ordering = ('-nombre',)


