from banco import Banco
from  cliente import Cliente
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente("Luiz", 30)
cliente2 = Cliente("Maria", 18)
cliente3 = Cliente("Joao", 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254132, 0)
conta3 = ContaPoupanca(1212, 254158, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('cliente nao autenticado')

print("********************************")

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('cliente nao autenticado')
