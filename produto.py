class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco 
    def __repr__(self):
        return f"Nome: {self.nome}, preço: {self.preco}, id: {self.id}"