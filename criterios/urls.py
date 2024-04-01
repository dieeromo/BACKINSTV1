from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.listCriterios),
    path('post/', views.postCriterio),
    path('put/', views.putCriterio),
    path('delete/', views.deleteCriterio),
    path('procesos/list/', views.listCriterios),
   
]