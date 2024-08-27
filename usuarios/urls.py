from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Rota padrão
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logar/', views.logar, name='logar'),
]
