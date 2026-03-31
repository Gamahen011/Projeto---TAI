from Classes.produto import Produto
from Classes.administrador import Administrador

from flask import Flask, request, Response, jsonify

adm = Administrador("adm")
app = Flask("meu site")

@app.route("/produto/alterar", methods=["PUT"])
def post_alterarProdutos():
    id = request.json["id"]
    nome = request.json["nome"]
    preco = request.json["preco"]
    produto = adm.alterarProduto(id, nome, preco)
    return str(produto)


@app.route("/produto/listar", methods=["GET"])
def post_listarProdutos(): 
    return str(adm.listarProdutos())

@app.route("/produto/cadastrar", methods=["POST"])
def post_cadastrarProdutos():
    nome = request.json["nome"]
    preco = request.json["preco"]
    adm.cadastrarProduto(nome, preco)  
    return "Cadastrado com sucesso"

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
def post_alterarProdutos():
    cpf = request.json["cpf"]
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    cliente = adm.alterarCliente(cpf, nome, email, senha)
    return str(cliente)


@app.route("/cliente/listar", methods=["GET"])
def post_listarCliente(): 
    return str(adm.listarCliente())

@app.route("/cliente/cadastrar", methods=["POST"])
def post_cadastrarProdutos():
    cpf = request.json["cpf"]
    nome = request.json["nome"]
    email = request.json["email"]
    senha = request.json["senha"]
    adm.cadastrarProduto(cpf, nome, email, senha)  
    return "Cadastrado com sucesso"

#@app.route("/cliente/deletar", methods=["DELETE"])
#def post_deletarCliente():
    



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
