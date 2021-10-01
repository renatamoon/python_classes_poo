#na composicao, uma classe pertence a outra classe
#A classe Endereço, pertence a classe Cliente

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] #receber objetos da classe endereço

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #chamando a classe Endereco
        #passa o cidade e estado - aqui estamos fazendo a composicao

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):#somente para quando sumir da memoria
        print(f'{self.nome} FOI APAGADO')
        # depois que os objetos foram usados, o __del__ apagou os objetos

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):  #depois que os objetos foram usados, o __del__ apagou os objetos
        print(f'{self.cidade}/{self.estado} FOI APAGADO')


cliente1 = Cliente("Renata", 32)
cliente1.insere_endereco("São Paulo", "SP")
print("Dados: ", cliente1.nome, cliente1.idade)
cliente1.lista_enderecos()
del cliente1 #mandou apagar
print("=*"*10)

cliente2 = Cliente("Leonardo", 39)
cliente2.insere_endereco("Salvador", "BA")
cliente2.insere_endereco("Rio de Janeiro", "RJ")
print("Dados: ", cliente2.nome, cliente2.idade)
cliente2.lista_enderecos()
del cliente2 #mandou apagar
print("=*"*10)

cliente3 = Cliente("Romano", 25)
cliente3.insere_endereco("Belo Horizonte", "MG")
print("Dados: ", cliente3.nome, cliente3.idade)
cliente3.lista_enderecos()
del cliente3 #mandou apagar
print("=*"*10)

print("#"*15) #aqui nao vai mostrar nada no garbage collector, pois já estou mandando
#apagar
