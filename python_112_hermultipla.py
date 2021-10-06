#HERANÇA MULTIPLA
#CLASSE MIXING - nao foi feita para ser instanciada diretamente, ela tem uma funcionaliddae
#adciional que será usada em outras classes e ela nao aparece na hierarquia de classes
"""
class A:
    def falar(self):
        print("Falando ... Estou em A")

class B(A): #herda tudo de A
    def falar(self):
        print("Falando ... Estou em B")

class C(A): #herda de A, e nao esta relacionada com B
    def falar(self):
        print("Falando ... Estou em C")

class D(B, C): #classe D tem tudo o que tem de B e C
    #busca da esquerda para direita
    def falar(self):
        print("Falando ... Estou em D")

d = D()
d.falar() #chama metodo de B, pois a ordem é B e C, e executa o metodo que foi solicitado
#se ele nao encontrar em B, ele procura o metodo falar em C, e se nao achar o metodo em C
#ele produra em A, pois C hera de A
 """
#EXEMPLO:

from python_112_log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome #protegido - oculto
        self._ligado = False #desligado

    def ligar(self):
        if self._ligado:
            return #nao executa nada, sai da funcao - retorna None
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return #nao executa nada, sai da funcao - retorna None
        self._ligado = False


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} FOI DESLIGADO COM SUCESSO'
        print(info)
        self.log_info(info)
        self._conectado = False

#programa principal

smartphone1 = Smartphone('Pocophone F1')
smartphone1.conectar()
smartphone1.desligar()
smartphone1.ligar()
smartphone1.conectar()
smartphone1.conectar()
smartphone1.conectar()
smartphone1.desligar()
smartphone1.conectar()
smartphone1.desconectar()
smartphone1.desconectar()

