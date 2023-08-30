from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

"""
Se definen las llamadas por url y las vistas que se ejecutaran.
"""
urlpatterns = [
    path('producto/', ProductoAPIView.as_view(), name='producto'),
    path('producto/<int:pk>/', ProductoAPIViewDetail.as_view()),
    path('pedido/', PedidoAPIView.as_view(), name='producto'),
    path('pedido/<int:pk>/', PedidoAPIViewDetail.as_view()),
    path('auth/', obtain_auth_token),
    path('login/', login, name='login'),
    path('logut/', logout_view, name='logut'),
    path('add_producto', add_producto_view, name='add_producto_view')
]
