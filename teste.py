from produto import Produto
from administrador import Administrador

from flask import Flask
from flask import request

adm = Administrador("adm")

app = Flask("meu site")
@app.route("/teste")
def teste():
    adm.cadastrarProduto(1, "Bola", 2)
    return str(adm.alterarProduto(1, "Manga", 10))
app.run()



