from django import forms
from .models import Administrador, Cliente, Produto, Carrinho


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Digite o nome do administrador",
                "class": "form-control"
            }),
        }


class ClienteForm(forms.ModelForm):
    administrador = forms.ModelChoiceField(
        queryset=Administrador.objects.all(),
        label="Administrador",
        empty_label="-- Selecione um administrador --"
    )
    
    class Meta:
        model = Cliente
        fields = ["administrador", "nome", "email", "senha"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Digite o nome do cliente",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Digite o email do cliente",
                "class": "form-control"
            }),
            "senha": forms.PasswordInput(attrs={
                "placeholder": "Digite a senha do cliente",
                "class": "form-control"
            }),
        }


class ProdutoForm(forms.ModelForm):
    administrador = forms.ModelChoiceField(
        queryset=Administrador.objects.all(),
        label="Administrador",
        empty_label="-- Selecione um administrador --"
    )
    
    class Meta:
        model = Produto
        fields = ["administrador", "nome", "preco"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Digite o nome do produto",
                "class": "form-control"
            }),
            "preco": forms.NumberInput(attrs={
                "placeholder": "Digite o preço do produto",
                "step": "0.01",
                "class": "form-control"
            }),
        }


class CarrinhoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label="Cliente",
        empty_label="-- Selecione um cliente --"
    )
    
    class Meta:
        model = Carrinho
        fields = ["cliente"]


class ProdutoCarrinhoForm(forms.Form):
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        label="Produto",
        empty_label="-- Selecione um produto --"
    )