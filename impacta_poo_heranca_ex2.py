#EXEMPLO 2

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)

    def depositar(self, valor):
        self.saldo += valor


class ContaEspecial(Conta): #herdando a Classe mae
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor): #considerando o limte da conta
        if (self.saldo + self.limite >= valor):
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

class Poupanca(Conta):
    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

    def calcular_juros(self):
        self.saldo += self.saldo * 0.005

#programa principal

conta_especial = ContaEspecial(1234,"Paulo", 1000, 200)
conta_poupanca = Poupanca(6789, "Maria", 2000)
print()
conta_especial.sacar(1100)
conta_especial.consultar_saldo()
print()
conta_poupanca.sacar(2100)
conta_poupanca.consultar_saldo()

