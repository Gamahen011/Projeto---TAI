from produto import Produto
from administrador import Administrador

from flask import Flask
from flask import request

adm = Administrador("adm")

app = Flask("meu site")
@app.route("/post", methods=["POST"])
def post_listarProdutos():
    id = request.json["id"]
    nome = request.json["nome"]
    preco = request.json["preco"]
    adm.cadastrarProduto(id, nome, preco)  
    return str(adm.listarProdutos())
app.run()

'''Post sem json
app = Flask("meu site")
@app.route("/post", methods=["POST"])
def post_listarProdutos():
    adm.cadastrarProduto(1, "Bola", 20)
    adm.cadastrarProduto(2, "Peixe", 25)
    adm.cadastrarProduto(3, "Casa", 2000)
    return str(adm.listarProdutos())
app.run()'''
