"""
PESSOA
nome = STR
idade = int
carro = Carro
-metodo = comprar carro(carro)

CARRO
marca = STR
Modelo = str
placa = str
ano = int
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro
        print("O CARRO COMPRADO FOI: ", self.carro.marca, self.carro.modelo, self.carro.placa, self.carro.ano)

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

carro1 = Carro("Chevrolet", "Camaro", "XXX-1020", 2018)

pessoa1 = Pessoa("Renata Monteiro", 25)

print("DADOS PESSOAIS DO COMPRODOR: ", pessoa1.nome, "--- IDADE: ", pessoa1.idade)
pessoa1.comprar_carro(carro1)



