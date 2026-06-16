from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Administrador, Cliente, Produto, Carrinho
from .forms import AdministradorForm, ClienteForm, ProdutoForm, CarrinhoForm

modelos = {
    'administrador': Administrador,
    'cliente': Cliente,
    'produto': Produto,
    'carrinho': Carrinho,
}

forms = {
    'administrador': AdministradorForm,
    'cliente': ClienteForm,
    'produto': ProdutoForm,
    'carrinho': CarrinhoForm,
}

campos = {
    'administrador': ['nome'],
    'cliente': ['administrador', 'nome', 'email'],
    'produto': ['administrador', 'nome', 'preco'],
    'carrinho': ['cliente'],
}

@require_http_methods(["GET"])
def home(request):
    return render(request, 'core/index.html')


@require_http_methods(["POST"])
def criar(request, categoria):
    if categoria not in modelos:
        return gerar_json(False, f'Categoria "{categoria}" não encontrada', status_code=404)
    
    formcategoria = forms[categoria]
    form, dados = normalizacao_form(request, formcategoria)
    
    if form.is_valid():
        obj = form.save()
        dados_resposta = model_todict(obj, campos[categoria])
        return gerar_json(True, f'{categoria} criado com sucesso', dados_resposta, 201)
    else:
        erros = dict(form.errors)
        return gerar_json(False, 'Erro na validação', erros, 400)


@require_http_methods(["GET"])
def listar(request, categoria):
    if categoria not in modelos:
        return gerar_json(False, f'Categoria "{categoria}" não encontrada', status_code=404)
    
    Model = modelos[categoria]
    valores = Model.objects.all().values()
    lista = list(valores) 
    
    return gerar_json(True, f'{categoria} listados com sucesso', lista)



@require_http_methods(["POST"]) # Depois mudar para Patch
def editar(request, categoria, id):
    if categoria not in modelos:
        return gerar_json(False, f'Categoria "{categoria}" não encontrada', status_code=404)
    
    Model = modelos[categoria]
    objeto = get_object_or_404(Model, id=id)
    
    FormClass = forms[categoria]
    form, dados = normalizacao_form(request, FormClass, objeto=objeto)
    
    if form.is_valid():
        objeto = form.save()
        dados_resposta = model_todict(objeto, campos[categoria])
        return gerar_json(True, f'{categoria} atualizado com sucesso', dados_resposta)
    else:
        erros = dict(form.errors)
        return gerar_json(False, 'Erro na validação', erros, 400)


@require_http_methods(["DELETE"])
def deletar(request, categoria, id):
    if categoria not in modelos:
        return gerar_json(False, f'Categoria "{categoria}" não encontrada', status_code=404)
    
    Model = modelos[categoria]
    objeto = get_object_or_404(Model, id=id)
    nome = str(objeto)
    objeto.delete()
    
    return gerar_json(True, f'{categoria} "{nome}" deletado com sucesso')



@require_http_methods(["GET"])
def opcoes_administrador(request):
    adms = Administrador.objects.all()
    dados = [{'id': adm.id, 'nome': adm.nome} for adm in adms]
    return gerar_json(True, 'Lista de Adms', dados)


@require_http_methods(["GET"])
def opcoes_cliente(request):
    clientes = Cliente.objects.all()
    dados = [{'id': cliente.id, 'nome': cliente.nome} for cliente in clientes]
    return gerar_json(True, 'Lista de Clientes', dados)



@require_http_methods(["GET"])
def carrinho_ver(request, id):
    carrinho = get_object_or_404(Carrinho, id=id)
    
    produtos = []
    total = 0
    
    for produto in carrinho.produtos.all():
        produtos.append({'id': produto.id, 'nome': produto.nome, 'preco': float(produto.preco)})
        total += float(produto.preco)
    
    dados = {'id': carrinho.id, 'cliente_id': carrinho.cliente.id, 'cliente_nome': carrinho.cliente.nome, 'produtos': produtos, 'total': round(total, 2)}
    
    return gerar_json(True, 'Lista Carrinho', dados)


@require_http_methods(["POST"])
def carrinho_adicionar(request, carrinho_id):
    carrinho = get_object_or_404(Carrinho, id=carrinho_id)
    
    try:
        data = json.loads(request.body)
        produto_id = data.get('produto_id')
    except (json.JSONDecodeError, KeyError):
        return gerar_json(False, 'produto_id é obrigatório', 400)
    
    produto = get_object_or_404(Produto, id=produto_id)
    
    if carrinho.produtos.filter(id=produto_id).exists():
        return gerar_json(False, 'Este produto já está no carrinho', 400)
    
    carrinho.produtos.add(produto)
    return gerar_json(True, f'Produto "{produto.nome}" adicionado ao carrinho')


@require_http_methods(["POST"])
def carrinho_remover(request, carrinho_id, produto_id):
    carrinho = get_object_or_404(Carrinho, id=carrinho_id)
    produto = get_object_or_404(Produto, id=produto_id)
    
    if not carrinho.produtos.filter(id=produto_id).exists():
        return gerar_json(False, 'Produto não está neste carrinho', 404)
    
    carrinho.produtos.remove(produto)
    return gerar_json(True, f'Produto "{produto.nome}" removido do carrinho')


# Funções uteis

def gerar_json(sucesso, mensagem, dados=None, status=200):
    if dados is None:
        dados = [] if sucesso else {}
    return JsonResponse({'sucesso': sucesso, 'mensagem': mensagem, 'dados': dados}, status=status)

def normalizacao_form(request, formcategoria, objeto=None):
    """Parse JSON body para dict e retorna instância do form"""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST
    
    if objeto:
        form = formcategoria(data, instance=objeto)
    else:
        form = formcategoria(data)
    
    return form, data


def model_todict(objeto, campos=None):
    if not objeto:
        return {}
    
    dict = {'id': objeto.id}
    
    if campos:
        for campo in campos:
            value = getattr(objeto, campo, None)
            
            # Se ForeignKey
            if hasattr(value, 'id'):
                dict[campo] = value.id
                dict[f'{campo}_nome'] = str(value)
            else:
                # Converter Decimal para float
                if hasattr(value, '__float__'):
                    dict[campo] = float(value)
                else:
                    dict[campo] = value
    return dict
