#class
#syntaxe

#marca, memoria ram, placa de video - tem todos esses atributos

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('estou desligando')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

#instanciar ela
computador1 = Computador('HP', '10gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()
# computador3 = Computador('Lenovo', '12gb', 'Nvidia')
# computador4 = Computador('Apple', '8gb', 'Raizen')



