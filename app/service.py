from .models import *

def add_producto_service(data):
    producto = Producto.objects.create(nombre=data.get('nombre'), precio=data.get('precio'),
                                      descripcion=data.get('descripcion'), stock=data.get('stock'))
    return {'producto': producto.nombre}

