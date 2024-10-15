from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UbicacionObras_ViewSet, CategoriasObras_ViewSet, TipoObras_ViewSet, AutoresObras_ViewSet
from .views import router , FilterObrasAutores_View,Obras_crud, listAutores
#from .viewsFilter import ObrasAutores_Filter_View

router = DefaultRouter()
router.register(r'ubicacion', UbicacionObras_ViewSet)
router.register(r'categorias', CategoriasObras_ViewSet)
router.register(r'tipo_obras', TipoObras_ViewSet)
router.register(r'autores', AutoresObras_ViewSet)
router.register(r'obras_crud', Obras_crud)


urlpatterns = [
    path('register/obra/', views.registroObra),
   
    path('list/categoria_obra/', views.listCategoria_obras),
    path('list/tipo_obras/', views.listTipo_obras),
    path('list/tipo_material/', views.listTipo_material),
    path('list/estado_obra/', views.listEstado_obra),
    path('list/obras/', views.filtro_obras_libros),
    path('obras/', include(router.urls)),

    path('register/autor/', views.registroAutor),
    
    path('list/autor/', listAutores.as_view()),
    #http://localhost:8002/biblioteca/list/autor/?autor=loto

    path('register/obraautor/', views.registerObraAutor),
    path('list/obras_autores/todos/', views.listAutores_obras_todos),  #devuelve todos loa auores y obras
    path('carga/obras/', views.uploadObraDocumento),  #
    path('filtro/autores/', views.FilterAutores_obras),  #d
    path('filtro/titulo/<str:titulo>/', views.FilterTitulo_obras),  #d
    path('filtro/titulo/id/<int:id>/', views.FilterTitulo_obras_id),  #d
    path('filtro/autor_por_obra/id/<int:id>/', views.FilterAutores_obras_idObra),  #d
    path('delete/obra_entrada/', views.deleteObraEntrada),  #d

    #path('filtro_todos_obras_autores', ObrasAutores_Filter_View.as_view(),),
    
    
    #se utiliza para enviar lops datos
    path('todas/obras/autores/', FilterObrasAutores_View.as_view(),),
    #http://localhost:8002/biblioteca/todas/obras/autores/?autor=&obra=
 
]
