from Classes.produto import Produto
from Classes.cliente import Cliente
from Classes.administrador import Administrador

from flask import Flask, request, Response, jsonify

adm = Administrador("adm")
app = Flask("meu site")


@app.route("/produto/alterar", methods=["PUT"])
def post_alterarProdutos():
    id = request.json["id"]
    nome = request.json["nome"]
    preco = request.json["preco"]
    try:
        if adm.alterarProduto(id, nome, preco):
            return Response("Produto alterado com sucesso", 200)
        else:
            return Response("Produto não encontrado", 404)
    except IndexError:
        return Response("Erro ao alterar produto", 500)
    

@app.route("/produto/listar", methods=["GET"])
def post_listarProdutos(): 
    return jsonify(adm.listarProdutos()), 200

@app.route("/produto/cadastrar", methods=["POST"])
def post_cadastrarProdutos():
    nome = request.json["nome"]
    preco = request.json["preco"]
<<<<<<< HEAD:Programa/rotas.py
    try: 
        adm.cadastrarProduto(nome, preco)  
        return Response("Produto Cadastrado", 200)
    except IndexError:
        return Response("Erro ao cadastrar produto", 500)
=======
    adm.cadastrarProduto(nome, preco)  
    return Response("Produto Cadastrado", 200)
>>>>>>> af1a25be993f91b934b3fba99bdb2e7899832260:Projeto---TAI/Programa/rotas.py

@app.route("/produto/deletar", methods=["DELETE"])
def post_deletarProdutos():
    id = request.json["id"]
    try:
        if id < 0 or adm.produtos[id] == None:
            return Response("ID não encontrado", 404)
        adm.deletarProduto(id)
        return Response("Produto deletada com sucesso", 200)
    except IndexError:
        return Response("Erro ao deletar produto", 500)
    

@app.route("/cliente/alterar", methods=["PUT"])
def post_alterarCliente():
<<<<<<< HEAD:Programa/rotas.py
    id = request.json["id"]
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    try:
        if adm.alterarCliente(id, nome, email, senha):
            return Response("Cliente alterado com sucesso", 200)
        else:
            return Response("Cliente não encontrado", 404)
    except IndexError:
        return Response("Erro ao alterar cliente", 500)
=======
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    cliente = adm.alterarCliente(nome, email, senha)
    return str(cliente)

>>>>>>> af1a25be993f91b934b3fba99bdb2e7899832260:Projeto---TAI/Programa/rotas.py

@app.route("/cliente/listar", methods=["GET"])
def post_listarCliente(): 
    return jsonify(adm.listarClientes()), 200

@app.route("/cliente/cadastrar", methods=["POST"])
def post_cadastrarCliente():
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
<<<<<<< HEAD:Programa/rotas.py
    try:
        adm.cadastrarCliente(nome, email, senha)  
        return Response("Cliente Cadastrado", 200)
    except IndexError:
        return Response("Erro ao cadastrar cliente", 500)

@app.route("/cliente/deletar", methods=["DELETE"])
def post_deletarCliente():
    id = request.json["id"]
    try:
        if id < 0 or adm.clientes[id] == None:
            return Response("ID não encontrado", 404)
        adm.deletarCliente(id)
        return Response("Cliente deletado com sucesso", 200)
    except IndexError:
        return Response("Erro ao deletar cliente", 500)

=======
    adm.cadastrarProduto(nome, email, senha)  
    return "Cadastrado com sucesso"

@app.route("/cliente/deletar", methods=["DELETE"])
def post_deletarCliente():
    id = request.json["id"]
    try:
        if id < 0 or adm.clientes[id] == None:
            return Response("ID não encontrado", 404)
        adm.deletarProduto(id)
        return Response("Produto deletada com sucesso", 200)
    except IndexError:
        return Response("Erro ao deletar produto", 500)
>>>>>>> af1a25be993f91b934b3fba99bdb2e7899832260:Projeto---TAI/Programa/rotas.py
    
app.run(debug=True)

'''Post sem json
app = Flask("meu site")
@app.route("/post", methods=["POST"])
def post_listarProdutos():
    adm.cadastrarProduto(1, "Bola", 20)
    adm.cadastrarProduto(2, "Peixe", 25)
    adm.cadastrarProduto(3, "Casa", 2000)
    return str(adm.listarProdutos())
app.run()'''