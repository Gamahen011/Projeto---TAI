from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Administrador, Cliente, Produto, Carrinho

categorias = {
    'produto': Produto,
    'cliente': Cliente,
    'carrinho': Carrinho,
    'administrador': Administrador
}

paginas = {
    'administrador': 'administrador/administrador.html',
    'administrador_criar': 'administrador/criar.html',

    'carrinho': 'carrinho/carrinho.html',

    'cliente': 'cliente/cliente.html',


    'produto': 'produto/produto.html',
    'produto_criar': 'produto/criar.html',


    'home': 'home.html',
}

def ler_pagina(request, nome):
    pagina = paginas.get(nome, '')
    if pagina == '':
        return JsonResponse({'status': 'false', 'mensagem': 'página não encontrada'}, status=404)
    return render(request, pagina, {'categoria': nome})


def cadastrar_categoria(request, categoria):
    if request.method != 'POST':
        return JsonResponse({'status': 'false', 'mensagem': 'Método não permitido'}, status=405)
    if categoria not in ['produto', 'cliente', 'carrinho', 'administrador']:
        return JsonResponse({'status': 'false', 'mensagem': 'Categoria inválida'}, status=400)
  
    model = categorias.get(categoria, "")
    
    match (categoria):
        case 'administrador':
            nome = request.POST.get("nome", "").strip()
            model.objects.create(nome=nome)
            return JsonResponse({'status': 'true'})

        case 'carrinho':
            cliente = request.POST.get("cliente", "").strip()
            dono = get_object_or_404(Cliente, id=cliente)
            model.objects.create(cliente=dono)
            return JsonResponse({'status': 'true'})

        case 'produto':
            adm = request.POST.get("adm", "").strip()
            nome = request.POST.get("nome", "").strip()
            preco = request.POST.get("preco", "").strip()
            dono = get_object_or_404(Administrador, id=adm)
            model.objects.create(administrador=dono, nome=nome, preco=preco)
            return JsonResponse({'status': 'true'})
        
        case 'cliente':
            adm = request.POST.get("adm", "").strip()
            nome = request.POST.get("nome", "").strip()
            email = request.POST.get("email", "").strip()
            senha = request.POST.get("senha", "").strip()
            dono = get_object_or_404(Administrador)
            model.objects.create(administrador=dono, nome=nome, email=email, senha=senha)
            return JsonResponse({'status': 'true'})



def listar_categoria(request, categoria, idpai):
    if categoria not in ['produto', 'cliente', 'carrinho', 'administrador']:
        return JsonResponse({'status': 'false', 'mensagem': 'Categoria inválida'}, status=400)

    if categoria == 'administrador':
        administradores = Administrador.objects.all()
        lista = []
        for adm in administradores:
            lista.append(adm)
        return render(request, 'listar.html', {'categoria': "administrador",'lista': lista})

    model = categorias.get(categoria, "")
    if categoria == 'carrinho':
        dono = get_object_or_404(Cliente, id=idpai)
        lista = model.objects.filter(cliente=dono)
    else:
        dono = get_object_or_404(Administrador, id=idpai)
        lista = model.objects.filter(administrador=dono)
    return render(request, 'listar.html', {'categoria': categoria, 'lista': lista})



    



    
   