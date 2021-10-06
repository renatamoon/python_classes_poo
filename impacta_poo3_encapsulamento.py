#ENCAPSULAMENTO
#atributos publicos - tem acesso fora da classe, e conseguem ser alterados
#quando trabalhamos com encapsulamento, esses elementos ficam ocultos, e não conseguem ter acesso
#fora da classe
#no caso isso serve para que seja criada uma camada de segurança para que o valor não seja alterado
#facilmente, oculta-se algumas informações

class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        #atributos publicos
        self.nome = nome #atributo publico
        self.idade = idade #atributo publico
        #atributos privados (começa com 2 underlines)
        #impactará porque agora estão ocultos dentro da minha classe - ficam encapsulados
        self.__cpf = cpf #atributo privado
        self.__rg = rg #atributo privado

    # def teste(self): #no caso, caso eu queira acessar um atributo dentro da classe eu posso, so
    #     #não posso fazer alguma alteração fora da classe
    #     self.__cpf
    #     self.__rg

    #o que podemos fazer para transformar esse atributo privado em publico é usando um metodo
    #para transformar esse atributo em publico, pois ele terá acesso a isso

    #GETTERS
    def get_cpf(self): #retorna o valor de um atributo privado e transforma ele em publico
        return self.__cpf

    def get_rg(self):
        return self.__rg

    #SETTERS - metodo que se usa para alterar, settar o valor do atributo
    #no caso aqui fazemos um metodo que receberá uma variavel, no caso cpf, e atribuirá o valor de
    #__cpf a ela - ai sim conseguimos fazer a alteração de um atributo privado
    def set_cpf(self, cpf):
        self.__cpf = cpf

#programa principal

pessoa1 = Pessoa("JOÃO", 25, "111111111111", "3333333")
pessoa1.idade = 26 #altera a idade
pessoa1.set_cpf("222222222222")
pessoa1.set_rg("44444444")#recebe o valor da variavel cpf, e altera o cpf

print("Nome: ", pessoa1.nome) #exibe o nome
#print("CPF", pessoa1.__cpf) #exibe o cpf - mas comoo cpf é privado, não consigo mais acessar
#mas podemos acessar o metodo Getter:
print("CPF: ", pessoa1.get_cpf()) #no caso ele pega o metodo get_cpf que transforma o atributo __cpf
#em publico
print("RG: ", pessoa1.get_rg())
