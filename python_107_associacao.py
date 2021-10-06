#ASSOCIACAO - ASSOCIADA A OUTRA CLASSE
#MAS AS CLASSES PODEM VIVER UMA SEM A OUTRA
from python_107 import Escritor
from python_107 import Caneta
from python_107 import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

#associando:
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print("A marca da caneta é: ", caneta.marca)
maquina.escrever()
