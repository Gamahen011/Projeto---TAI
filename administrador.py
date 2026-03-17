from produto import Produto

class Administrador:
    def __init__(self, nome):
        self.nome = nome

        

    def cadastrarProduto(self, id, nome, preco):
        novoProduto = Produto(id, nome, preco)
        return novoProduto
