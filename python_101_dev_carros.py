class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def dar_partida(self):
        print(f'O carro {self.modelo} está dando partida agora')
        return

    def parar_carro(self):
        print(f'O carro {self.modelo} está parando')

    def carro_quebrou(self):
        print(f'O carro {self.modelo} está quebrado')

    def InformacoesDoCarro(self):
        print(self.marca, self.modelo, self.ano, self.preco)

carro1 = Carro('chevrolet', 'Camaro', '2018', 'R$ 23.000')

carro1.InformacoesDoCarro()
carro1.dar_partida()
carro1.parar_carro()
carro1.carro_quebrou()