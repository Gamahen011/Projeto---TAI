from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('<int:idpai>/<slug:categoria>/cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'), # Para adm, defina idpai como 0

    path('<int:idpai>/<slug:categoria>/listar/', views.listar_categoria, name='listar_categoria'), # Para adm, defina idpai como 0
]
