class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf #privado
        self.__senha = senha #privado
        self.__saldo = 0 #privado

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

    def set_cpf(self, cpf):
        self.__cpf = cpf


class ContaBancaria:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero #associado à Conta
        self.cliente = cliente
        self.__saldo = saldo #iniciar saldo em 0

    def __validacao_de_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            print("ERRO: SENHA INVALIDA")
            return False

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha): #adiciona o valor imputado do saldo
        if self.__validacao_de_senha(senha) is True:
            self.__saldo = self.__saldo + valor


    def sacar(self, valor, senha): #subtrai o valor imputado do saldo
        if self.__validacao_de_senha(senha) is True:
            self.__saldo -= valor


#PROGRAMA PRINCIPAL

cliente1 = Cliente('Renata Monteiro', '424911014-80', 123)
conta1 = ContaBancaria(14520, 'Renata Monteiro', 0)

valor = float(input("QUAL VALOR QUER DEPOSITAR: R$ "))
senha = int(input("DIGITE SUA SENHA PARA EFETUAR A OPERAÇÃO: "))

conta1.depositar(valor, senha)
print("SALDO ATUAL: ", conta1.get_saldo())