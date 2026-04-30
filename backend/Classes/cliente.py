class Cliente:
    id_contador = 0
    def __init__ (self, nome, email, senha, adm):
        self.id = Cliente.id_contador
        self.nome = nome
        self.email = email
        self.senha = senha
        self.adm = adm
        self.carrinho = []
        Cliente.id_contador += 1
    
    def __repr__(self):
        return str(f"Nome: {self.nome}, email: {self.email}, senha: {self.senha}, id:{self.id}, adm: {self.adm.nome}")
    
    def colocarCarrinho(self, idproduto):
        for i in self.adm.produtos:
            if i.id == idproduto:
                self.carrinho.append(i)
                return True
        return False
    
    def listarCarrinho(self):
        lista = []
        for i in self.carrinho:
            lista.append(i.to_dict())
        return lista
    
    def removerCarrinho(self, idproduto):
        for i in self.carrinho:
            if i.id == idproduto:
                self.carrinho.remove(i)
                return True
        return False
    
    def finalizarCompra(self):
        preco = 0
        for i in self.carrinho:
            preco += i.preco
        return preco

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "adm": self.adm.nome
        }
