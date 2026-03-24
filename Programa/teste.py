from Classes.produto import Produto
from Classes.administrador import Administrador
from Classes.cliente import Cliente

adm = Administrador("adm")
adm.cadastrarProduto("Maca", 10)
cliente = Cliente("João", "joazingameplays@slameu", "34567-0985", "Sim")

print(cliente.colocarCarrinho("Maca", adm))
