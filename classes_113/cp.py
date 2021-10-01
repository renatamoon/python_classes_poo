#CONTA POUPANÇA
from classes_113.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("SALDO INSUFICIENTE")
            return

        self.saldo -= valor #retirando do valor
        self.get_detalhes()