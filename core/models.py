from django.db import models

class Administrador(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=True) # Dps colocar no login, assim pra testar

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}'

class Produto(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Nome: {self.nome}, Preço: R${self.preco}'
    
class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        produtos = ", ".join([produto.nome for produto in self.produtos.all()])
        return f"Carrinho de {self.cliente.nome}, Produtos: {produtos}"