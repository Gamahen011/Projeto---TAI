from Classes.produto import Produto
from Classes.cliente import Cliente

class Administrador:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
        self.clientes = []

    def cadastrarProduto(self, nome, preco): 
        self.produtos.append(Produto(nome, preco, self))
        return True

    def alterarProduto(self, id, novonome, novopreco):
        for i in self.produtos:
            if id == i.id:
                i.nome = novonome
                i.preco = novopreco
                return True
        return False
    
    def listarProdutos(self):
        lista = []
        for i in self.produtos:
            lista.append(i.to_dict())
        return lista
    
    def deletarProduto(self, id):
        for i in self.produtos:
            if id == i.id:
                self.produtos.remove(i)
                return True
        return False
    
    def cadastrarCliente(self, nome, email, senha): 
        self.clientes.append(Cliente(nome, email, senha, self))
        return True

    def alterarCliente(self, id, novonome, novoemail, novasenha):
        for i in self.clientes:
            if id == i.id:
                i.nome = novonome
                i.email = novoemail
                i.senha = novasenha
                return True
        return False
    
    def listarClientes(self):
        lista = []
        for i in self.clientes:
            lista.append(i.to_dict())
        return lista
    
    def deletarCliente(self, id):
        for i in self.clientes:
            if id == i.id:
                self.clientes.remove(i)
                return True
        return False
    