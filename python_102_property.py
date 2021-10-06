# @property
# Getters - obtem um valor
# Setters - seta um valor

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter #configurando o valor do nome para ser maiusculo, ou capital, ou substituir valores
    def nome(self, valor):
        self._nome = valor.replace('A', '@')

    #getter - obter um valor - #decorador - vamos criar um metodo que estará decorado pelo property
    @property
    def preco(self):
        return self._preco

    #SETTER - criadno um setter - irá configuar o preço
    @preco.setter #irá retirar o R$ do valor e passará de str para float
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('CAMISETA', 50) #atribuindo os valores para Produto - p1
p1.desconto(10) #atribuindo o valor de desconto para p1
print(p1.nome, p1.preco) #pedindo para mostrar o preço depois de atribuir o desconto


p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

#como eu configurei o R$ para ser retirado lá no setter do preço
#então ele receberá no final, mesmo nao recebendo um numero, e sim uma
# str, o setter passará o valor de str pra float


