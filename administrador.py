from produto import Produto

class Administrador:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def cadastrarProduto(self, id, nome, preco): 
        self.produtos.append(Produto(id, nome, preco))
        return Produto(id, nome, preco)

    def alterarProduto(self, id, novonome, novopreco):
        for i in self.produtos:
            if id == i.id:
                i.nome = novonome
                i.preco = novopreco
        return Produto(id, novonome, novopreco)
    
    def listarProdutos(self):
        post = ""
        for i in self.produtos:
            post += str(i) + ";" + "\n"
        return post