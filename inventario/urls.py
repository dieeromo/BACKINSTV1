from django.urls import path, include
from . import views
from .views import router


urlpatterns = [
    #EndPoint  para listar tipo de inventario
    path('list_tipo/', views.list_tipoInventario),
    #EndPoint  para listar estado de inventario
    path('list_estado/', views.list_estadoInventario),
    #EndPoint  para listar ubicacion de inventario
    path('list_ubicacion/', views.list_ubicacionInventario),

    path('list_inventario/', views.list_inventarioIST),
    path('register_inventario/', views.register_inventario),

     path('ist/', include(router.urls)),

]