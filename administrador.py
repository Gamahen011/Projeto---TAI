from produto import Produto

class Administrador:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def cadastrarProduto(self, id, nome, preco):
        self.produtos.append(Produto(id, nome, preco))
        
