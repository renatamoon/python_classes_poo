#sobreposição de membros e metodos(atributos e metodos)
#especializando as classes

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

    def falar(self):
        print("ESTOU EM CLIENTE")

class Aluno(Pessoa): #herdando os atributos de pessoa / Aluno é uma Pessoa
    def estudar(self):
        print(f'{self.nomeclasse} está estudando ...')

class ClienteVIP(Cliente):
    #no caso tudo o que tem em Cliente VIP tem na Cliente, e que tem também em Pessoa.
    #pois herda os metodos das classe
    #sobrescrevendo o metodo falar em Pessoa
    # def falar(self):
    #     Pessoa.falar(self) #pedindo para que seja executado o metodo falar da Classe Super
    #     #e depois o o Cliente vip vai executar o def falar do Cliente VIP. Print abaixo:
    #     Cliente.falar(self)
    #     print("falando outra coisa qualquer").
    def __init__(self, nome, idade, sobrenome): #repassar o que tem em Cliente VIP para a Pessao
        super().__init__(nome, idade) #chamando o contrutor da superClasse Pessoa
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

#programa principal

cliente1 = Cliente("Luiz", 32)
cliente1.comprar()

print()

cliente2 = ClienteVIP('Rosa', 25, 'Miranda')
cliente2.falar()

