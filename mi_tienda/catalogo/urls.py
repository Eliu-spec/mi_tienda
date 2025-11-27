from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.lista_productos, name='lista'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle'),
]