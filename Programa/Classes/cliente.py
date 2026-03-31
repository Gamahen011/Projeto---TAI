from Classes.produto import Produto
from Classes.administrador import Administrador

class Cliente:
    def __init__ (self, cpf, nome, email, senha):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carrinho = []
    
    def __repr__(self):
        return str(f"Nome: {self.nome}, email: {self.email}, senha: {self.senha}, cpf: {self.cpf}")
    
    def colocarCarrinho(self, nomeproduto, adm):
        for i in adm.produtos:
            if adm.produtos.nome == nomeproduto:
                self.carrinho.append(i)
                return True
        return False
    


