from getpass import getpass
#importando um metodo onde se digitar uma senha ela não aparece no terminal, ela fica oculta

class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha #privado
        self.__saldo = 0 #privado

    def __validar_senha(self, senha): #METODO PRIVADO "__" NA FRENTE
        if senha == self.__senha:
            return True
        else:
            print("ERRO: SENHA INVALIDA")
            return False

    def depositar(self, valor, senha): #solicita um valor
        if self.__validar_senha(senha) is True: #so consegue fazer a operacao, se a senha for igual
            self.__saldo += valor

    def sacar(self, valor, senha): #solicita um valor
        if self.__validar_senha(senha) is True:
            self.__saldo -= valor #decrementar o valor do saldo

    def consultar_saldo(self): #exibir o saldo
        return self.__saldo

#OPERAÇÃO DE DEPOSITO
                    #conta    #Titular       #senha
conta1 = ContaBancaria(1234, "Paulo Vieira", 123)

valor = float(input("Valor para Deposito: R$ ")) #pedindo para o user imputar o valor
senha = int(getpass("Digite a sua senha: ")) #colocando o getpass
conta1.depositar(valor, senha) #o valor informado vai para o metodo depositar

print("Saldo atual: ", conta1.consultar_saldo()) #usando o metodo consultar

#OPERAÇÃO DE SAQUE

valor = float(input("Valor para Saque: R$ ")) #pedindo para o user imputar o valor
senha = int(getpass("Digite a sua senha: ")) #colocando o getpass
conta1.sacar(valor, senha)
print("Saldo atual: ", conta1.consultar_saldo())

