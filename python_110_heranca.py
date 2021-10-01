#APRENDEREMOS HERANÇA - ONDE UM OBJETO É OUTRO OBJETO
#a herança funciona de cima para baixo. A pessoa é quem decidiu os metodos principais para as
#outras classes. O CLIENTE E ALUNO é uma melhoria da classe Pessoa, é mais especializado.
#enquanto a Pessoa pode ser usada por qualquer classe, as outras subclasses (Cliente, Aluno)
#não podem pegar metodos da Classe Cliente e vice versa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__ #chamando o nome da classe que está usando
        # a classe

    def falar(self):
        print(f'{self.nomeclasse} está falando ...')

class Cliente(Pessoa): #herdando os atributos de pessoa / cliente é uma Pessoa
    def comprar(self):
        print(f'{self.nomeclasse} está comprando ...')

class Aluno(Pessoa): #herdando os atributos de pessoa / Aluno é uma Pessoa
    def estudar(self):
        print(f'{self.nomeclasse} está estudando ...')


cliente1 = Cliente("Renata", 25)
print(cliente1.nome)
#cliente1.falar()
cliente1.comprar()

aluno1 = Aluno("Maria", 40)
print(aluno1.nome)
#aluno1.falar()
aluno1.estudar()

p1 = Pessoa('João', 43)
p1.falar() #a Pessoa somente herdou o metodo falar, não herdou o estudar nem o comprar. 

