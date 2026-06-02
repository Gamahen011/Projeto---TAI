from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Administrador, Cliente, Produto, Carrinho

categorias = {
    'produto': Produto,
    'cliente': Cliente,
    'carrinho': Carrinho,
    'administrador': Administrador
}

def home(request):
    return render(request, 'home.html')

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


def cadastrar_categoria(request, categoria, idpai):
    if request.method != 'POST':
        return JsonResponse({'status': 'false', 'mensagem': 'Método não permitido'}, status=405)
    if categoria not in ['produto', 'cliente', 'carrinho', 'administrador']:
        return JsonResponse({'status': 'false', 'mensagem': 'Categoria inválida'}, status=400)
    
    model = categorias.get(categoria, "")
    
    if categoria == 'administrador':
        model.objects.create(nome="")
        return JsonResponse({'status': 'true'})

    elif categoria == 'carrinho':
        dono = get_object_or_404(Cliente, id=idpai)
        model.objects.create(cliente=dono)
        return JsonResponse({'status': 'true'})

    else:
        dono = get_object_or_404(Administrador, id=idpai)
        model.objects.create(administrador=dono, nome="")
        return JsonResponse({'status': 'true'})
    
   