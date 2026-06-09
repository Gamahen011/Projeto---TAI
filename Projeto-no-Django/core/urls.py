from django.urls import path
from . import views

urlpatterns = [

    path('<slug:categoria>/cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'), 
    path('<int:idpai>/<slug:categoria>/listar/', views.listar_categoria, name='listar_categoria'), # Para adm, defina idpai como 0


    path('<str:nome>/', views.ler_pagina, name='ler_pagina'),
]
