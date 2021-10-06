
class CarroCorrida:
    def __init__(self, numero,  piloto, velocidade_max, velocidade_atual, ligado=bool):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        print(f'O carro numero {self.__numero} está ligado {self.__ligado}')

    def desligar(self):
        print(f'O carro numero {self.__numero} está desligado')

    def velocidade_maxima(self):
        self.__velocidade_atual = []

    def acelerar(self,velocidadeatual):
        self.__velocidade_atual.append(velocidadeatual)

#programa principal

carro1 = CarroCorrida(20, 'Rodrigo Constantino', 90, 0)

carro1.ligar()
carro1.acelerar(20)