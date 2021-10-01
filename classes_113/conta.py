from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)): #checando se o valor é inteiro ou float
            raise ValueError("Saldo precisa ser numerico")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):  # checando se o valor é inteiro ou float
            raise ValueError("Valor do deposito precisa ser numerico")

        self._saldo += valor #cada vez que deposito incluo o valor dentro do saldo
        self.get_detalhes()


    def get_detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
