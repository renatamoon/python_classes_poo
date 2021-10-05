#HERANÇA
#criação de uma classe a partir de uma classe já existente

#herdar atributos e metodos publicos de outra
#reutilização de codigos
#tudo o que for publico vai ser herdado pelas classes filhas

class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    #metodo
    def exibir_dados(self):
        print("Marca do carro:", self.marca)
        print("Modelo do carro:", self.modelo)
        print("Placa do carro: ", self.placa)

class Carro(Veiculo): #herdando da classe VEICULO
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa) #referencia a super classe (chamando a super classe Veiculo e
        self.portas = portas

    def exibir_dados(self):
        super().exibir_dados() #herdando da classe mae Veiculo
        print("Portas: ", self.portas)

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, cilindradas):
        super().__init__( marca, modelo, placa) #herdando da classe mae
        self.cilindradas = cilindradas

    def exibir_dados(self):
        super().exibir_dados()
        print("Cilindradas: ", self.cilindradas)

    def andar(self):
        print("MOTO ESTÁ ANDANDO")

#programa principal

carro1 = Carro('VW', 'Tiguan', 'xyz-8954', 4)
carro1.exibir_dados()

print()

moto1 = Moto("Honda", "Biz", "BBB-3584", 1000)
moto1.exibir_dados()

