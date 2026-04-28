from Classes.produto import Produto
from Classes.cliente import Cliente
from Classes.administrador import Administrador

from flask import Flask, request, Response, jsonify, redirect, url_for

adm = Administrador("Nome do supermercado")
app = Flask("meu site")


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    return response

@app.route("/", methods=["GET"])
def get_menu():
    return redirect(url_for("get_listarProdutos"))

@app.route("/produto/alterar", methods=["PUT"])
def put_alterarProdutos():
    id = request.json["id"]
    nome = request.json["nome"]
    preco = request.json["preco"]
    try:
        if adm.alterarProduto(id, nome, preco):
            return Response("Produto alterado com sucesso", 200)
        return Response("Produto não encontrado", 404)
    except IndexError:
        return Response("Erro ao alterar produto", 500)
    
@app.route("/produto/listar", methods=["GET"])
def get_listarProdutos(): 
    if adm.produtos == []:
        return Response("Nenhum produto cadastrado", 200)
    return jsonify(adm.listarProdutos()), 200

@app.route("/produto/cadastrar", methods=["POST"])
def post_cadastrarProdutos():
    nome = request.json["nome"]
    preco = request.json["preco"]
    try: 
        if adm.cadastrarProduto(nome, preco):  
            return Response("Produto Cadastrado", 200)
        return Response("Erro ao cadastrar produto", 500)
    except IndexError:
        return Response("Erro ao cadastrar produto", 500)

@app.route("/produto/deletar", methods=["DELETE"])
def delete_deletarProdutos():
    id = request.json["id"]
    try:
        if adm.deletarProduto(id):        
            return Response("Produto deletado com sucesso", 200)
        return Response("Produto não encontrado", 404)
    except IndexError:
        return Response("Erro ao deletar produto", 500)
    

@app.route("/cliente/alterar", methods=["PUT"])
def put_alterarCliente():
    id = request.json["id"]
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    try:
        if adm.alterarCliente(id, nome, email, senha):
            return Response("Cliente alterado com sucesso", 200)
        return Response("Cliente não encontrado", 404)
    except IndexError:
        return Response("Erro ao alterar cliente", 500)

@app.route("/cliente/listar", methods=["GET"])
def get_listarCliente():
    if adm.clientes == []:
        return Response("Nenhum cliente cadastrado", 200) 
    return jsonify(adm.listarClientes()), 200

@app.route("/cliente/cadastrar", methods=["POST"])
def post_cadastrarCliente():
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    try:
        if adm.cadastrarCliente(nome, email, senha):
            return Response("Cliente Cadastrado", 200)
        return Response("Erro ao cadastrar cliente", 500)
    except IndexError:
        return Response("Erro ao cadastrar cliente", 500)

@app.route("/cliente/deletar", methods=["DELETE"])
def delete_deletarCliente():
    id = request.json["id"]
    try:
        if adm.deletarCliente(id):
            return Response("Cliente deletado com sucesso", 200)
        return Response("Cliente não encontrado", 404)
    except IndexError:
        return Response("Erro ao deletar cliente", 500)
    
@app.route("/cliente/colocarCarrinho", methods=["POST"])
def post_colocarCarrinho():
    idcliente = request.json["idcliente"]
    idproduto = request.json["idproduto"]
    for i in adm.clientes:
        if idcliente == i.id:
            if i.colocarCarrinho(idproduto):
                return Response("Produto adicionado ao carrinho", 200)
            return Response("Produto não encontrado", 404)
    return Response("Cliente não encontrado", 404)

@app.route("/cliente/listarCarrinho", methods=["GET"])
def get_listarCarrinho():
    id = request.json["id"]
    for i in adm.clientes:
        if id == i.id:
            if i.carrinho == []:
                return Response("Nenhum produto no carrinho", 200)
            return jsonify(i.listarCarrinho()), 200
    return Response("Cliente não encontrado", 404)

@app.route("/cliente/removerCarrinho", methods=["POST"])
def post_removerCarrinho():
    idcliente = request.json["idcliente"]
    idproduto = request.json["idproduto"]
    for i in adm.clientes:
        if idcliente == i.id:
            if i.removerCarrinho(idproduto):
                return Response("Produto removido do carrinho", 200)
            return Response("Produto não encontrado no carrinho", 404)
    return Response("Cliente não encontrado", 404)

@app.route("/cliente/finalizarCompra", methods=["POST"])
def post_finalizarCompra():
    id = request.json["id"]
    for i in adm.clientes:
        if id == i.id:
            if i.carrinho == []:
                return Response("Nenhum produto no carrinho", 200)
            preco = i.finalizarCompra()
            return Response(f"Compra finalizada, preço total: {preco}", 200)
    return Response("Cliente não encontrado", 404)

app.run(debug=True, host="0.0.0.0", port=5000)


'''Post sem json
app = Flask("meu site")
@app.route("/post", methods=["POST"])
def post_listarProdutos():
    adm.cadastrarProduto("Bola", 20)
    adm.cadastrarProduto("Peixe", 25)
    adm.cadastrarProduto("Casa", 2000)
    return str(adm.listarProdutos())
app.run()'''