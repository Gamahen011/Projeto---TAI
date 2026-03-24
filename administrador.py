from produto import Produto

class Administrador:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def cadastrarProduto(self, nome, preco): 
        produto = self.produtos.append(Produto(nome, preco))
        return produto

    def alterarProduto(self, id, novonome, novopreco):
        for i in self.produtos:
            if id == i.id:
                i.nome = novonome
                i.preco = novopreco
                return str(i)
    
    def listarProdutos(self):
        post = ""
        for i in self.produtos:
            post += str(i) + ";" + "\n"
        return post