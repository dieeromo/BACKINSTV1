from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.listCriterios),
    path('procesos/list/', views.listCriterios),
]