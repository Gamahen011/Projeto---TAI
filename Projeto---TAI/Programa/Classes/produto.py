class Produto:
    id_contador = 0
    def __init__(self, nome, preco):
        self.id = Produto.id_contador
        self.nome = nome
        self.preco = preco
        Produto.id_contador += 1 
    def __repr__(self):
        return str(f"'id': {self.id}, 'nome': {self.nome}, 'preço': {self.preco}")
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco
        }