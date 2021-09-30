#ENCAPSULAMENTO
#atributos publicos - tem acesso fora da classe, e conseguem ser alterados
#quando trabalhamos com encapsulamento, esses elementos ficam ocultos, e não conseguem ter acesso
#fora da classe
#no caso isso serve para que seja criada uma camada de segurança para que o valor não seja alterado
#facilmente, oculta-se algumas informações

class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        #atributos publicos
        self.nome = nome
        self.idade = idade
        #atributos privados (começa com 2 underlines)
        #impactará porque agora estão ocultos dentro da minha classe - ficam encapsulados
        self.__cpf = cpf
        self.__rg = rg

    # def teste(self): #no caso, caso eu queira acessar um atributo dentro da classe eu posso, so
    #     #não posso fazer alguma alteração fora da classe
    #     self.__cpf
    #     self.__rg

#programa principal

pessoa1 = Pessoa("JOÃO", 25, "111111111111", "3333333")
pessoa1.idade = 26 #altera a idade
#pessoa1.__cpf = "222222222222" #altera o cpf

print("Nome", pessoa1.nome) #exibe o nome
#print("CPF", pessoa1.__cpf) #exibe o cpf