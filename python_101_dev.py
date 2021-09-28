#class
#syntaxe

#marca, memoria ram, placa de video - tem todos esses atributos

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass
#instanciar ela
computador1 = Computador('HP', '10gb', 'Nvidia')
computador3 = Computador('Lenovo', '12gb', 'Nvidia')
computador4 = Computador('Apple', '8gb', 'Raizen')

print(computador1.marca, computador1.memoria_ram, computador1.memoria_ram)

