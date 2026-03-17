from produto import Produto
from administrador import Administrador

from flask import Flask

adm = Administrador("adm")

app = Flask("meu site")
@app.route("/teste")
def teste():
    return str(adm.cadastrarProduto(1, "Bola", 2))
app.run()



