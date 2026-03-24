from Classes.produto import Produto
from Classes.administrador import Administrador

from flask import Flask
from flask import request

adm = Administrador("adm")
app = Flask("meu site")

@app.route("/alterar", methods=["POST"])
def post_alterarProdutos():
    id = request.json["id"]
    nome = request.json["nome"]
    preco = request.json["preco"]
    produto = adm.alterarProduto(id, nome, preco)
    return str(produto)


@app.route("/listar", methods=["POST"])
def post_listarProdutos(): 
    return str(adm.listarProdutos())

@app.route("/cadastrar", methods=["POST"])
def post_cadastrarProdutos():
    nome = request.json["nome"]
    preco = request.json["preco"]
    adm.cadastrarProduto(nome, preco)  
    return str(adm.listarProdutos())

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
