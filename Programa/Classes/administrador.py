from Classes.produto import Produto
from Classes.cliente import Cliente

class Administrador:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
        self.clientes = []

    def cadastrarProduto(self, nome, preco): 
        self.produtos.append(Produto(nome, preco))
        return True

    def alterarProduto(self, id, novonome, novopreco):
        for i in self.produtos:
            if id == i.id:
                i.nome = novonome
                i.preco = novopreco
                return True
    
    def listarProdutos(self):
        lista = ""
        for i in self.produtos:
            lista += str(i) + ";" + "\n"
        return lista
    
    def deletarProduto(self, id):
        for i in self.produtos:
            if id == i.id:
                self.produtos.pop(id)
                return True
    
    def cadastrarCliente(self, cpf, nome, email, senha): 
        self.clientes.append(Cliente(cpf, nome, email, senha))
        return True

    def alterarCliente(self, cpf, novonome, novoemail, novasenha):
        for i in self.clientes:
            if cpf == i.cpf:
                i.nome = novonome
                i.email = novoemail
                i.senha = novasenha
                return True
    
    def listarCliente(self):
        lista = ""
        for i in self.produtos:
            listar += str(i) + ";" + "\n"
        return lista
    
    def deletarCliente(self, cpf):
        for i in self.clientes:
            if cpf == i.cpf:
                self.clientes.remove(cpf)
                return True
    
