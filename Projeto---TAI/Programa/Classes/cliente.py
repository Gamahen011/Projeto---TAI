class Cliente:
    id_contador = 0
    def __init__ (self, nome, email, senha):
        self.id = Cliente.id_contador
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carrinho = []
        Cliente.id.contador += 1
    
    def __repr__(self):
        return str(f"Nome: {self.nome}, email: {self.email}, senha: {self.senha}")
    
    def colocarCarrinho(self, nomeproduto, adm):
        for i in adm.produtos:
            if adm.produtos.nome == nomeproduto:
                self.carrinho.append(i)
                return True
        return False
    
    def listarCarrinho(self):
        lista = ""
        for i in self.carrinho:
            lista += str(i) + ";" + "\n"
        return lista

    


