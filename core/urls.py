from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    

    path('<slug:categoria>/criar/', views.criar, name='criar'),
    path('<slug:categoria>/', views.listar, name='listar'),
    path('<slug:categoria>/<int:id>/editar/', views.editar, name='editar'),
    path('<slug:categoria>/<int:id>/deletar/', views.deletar, name='deletar'),
    

    path('opcoes/administrador/', views.opcoes_administrador, name='opcoes_administrador'),
    path('opcoes/cliente/', views.opcoes_cliente, name='opcoes_cliente'),
    

    path('carrinho/<int:id>/ver/', views.carrinho_ver, name='carrinho_ver'),
    path('carrinho/<int:carrinho_id>/adicionar/', views.carrinho_adicionar, name='carrinho_adicionar'),
    path('carrinho/<int:carrinho_id>/remover/<int:produto_id>/', views.carrinho_remover, name='carrinho_remover'),
]
