from classes_113.cp import ContaPoupanca
from classes_113.cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print("#######################")

cc = ContaCorrente(agencia=1111, conta=33333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250) #fica negativo - 150
cc.sacar(500) #saldo insuficiente pois ultrapassa limite de saque
cc.depositar(1000)



