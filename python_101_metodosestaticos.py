#metodos estaticos
from random import randint
class Pessoa1:
    ano_atual = 2019 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod #decorar o metodo da classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod #metodos estaticos - isso é um decorador
        #como se fosse uma funcaom mas ela precisa estar dentro de uma classe
    #gerando um estatic method, nao podemos usar nem cls, nem self
    def gera_id():
        rand = randint(10000, 19999)
        return "O numero do Id gerado é: ", rand



p1 = Pessoa1.por_ano_nascimento('Luiz', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa1.gera_id()) #pedindo para dentro da classe Pessoa1 gerar
#um numero id com 5 digitos

