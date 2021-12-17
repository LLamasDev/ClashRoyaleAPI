from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfilinfo/<str:usuario>/', views.perfilinfo, name='perfilinfo'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('buscar/', views.buscar, name='buscar'),
    path('api/', views.JugadorAPI.as_view(), name='api'),
]