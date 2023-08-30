from django.shortcuts import render, redirect
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from .service import add_producto_service


# Create your views here.
class ProductoAPIView(APIView):
    """
    Vista que permite las funciones GET de todas instancias y POST con el Modelo de Producto
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        post = Producto.objects.all()
        serializer = ProductoSerializer(post, many=True)
        return render(request, 'list_products.html', {'productos': serializer.data})


class ProductoAPIViewDetail(APIView):
    """
    Vista que permite las funciones GET de un Producto en especifico, asi como el PUT y el DELETE
    """
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def login(request):
    error_message = ''
    if request.user.is_authenticated:
        return redirect(reverse('login'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            return redirect(reverse('producto'))
        else:
            error_message = "Usuario y/o contraseña incorrectos"

    context = {
        'error_message': error_message
    }
    if request.GET.get('next') is not None:
        context['next'] = request.GET.get('next')
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_producto_view(request):
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producto = add_producto_service(serializer.validated_data)
        return render(request, "add_products.html", producto)
    elif request.method == 'GET':
        return render(request, "add_products.html")


class PedidoAPIView(APIView):
    """
    Vista que permite las funciones GET de todas instancias y POST con el Modelo de PEDIDO
    """
    def get(self, request, *args, **kwargs):
        post = Pedido.objects.all()
        serializer = PedidoSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PedidoAPIViewDetail(APIView):
    """
    Vista que permite las funciones GET de un Pedido en especifico, asi como el PUT y el DELETE
    """
    def get_object(self, pk):
        try:
            return Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    def put(self, request, pk):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pedido = self.get_object(pk)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)