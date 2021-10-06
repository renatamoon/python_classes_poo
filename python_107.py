class Escritor:
    def __init__(self, nome): #quer que o atributo fique privado
        self.__nome = nome #__ dizedo que é privado
        self.__ferramenta = None #POODE RECEBER QUALQUER COISA
        #criando um getter
    @property
    def nome(self):
        return self.__nome

    @property #getter
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter #setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo ...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo ...')
