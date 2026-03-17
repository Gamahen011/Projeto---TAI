from produto import Produto
from administrador import Administrador

from flask import Flask



app = Flask("meu site")
@app.route("/teste")
def teste():
    produto = Produto(1, "bola", 10)
    sla = str(produto)
    return sla
app.run()

#adm = Administrador("Adm")
#print(adm.cadastrarProduto(1, "Bola", 10))


