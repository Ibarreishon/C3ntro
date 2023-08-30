from rest_framework import serializers
from .models import *


class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializer para validar campos y verificar que campos se recibiran y regresaran en las consultas.
    """

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock']

    def validate(self, data):
        # Se valida que los datos enviados de cantidad y precio sean correctos, si no lanza una excepcion y no se puede continuar
        existencia = data.get('stock')
        precio = data.get('precio')
        if existencia:
            if existencia < 0:
                raise serializers.ValidationError({"stock": "El stock no puede ser un numero negativo"})
        if precio:
            if precio < 0:
                raise serializers.ValidationError({"precio": "El precio no puede ser negativo"})
        return data


class PedidoSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'productos']
