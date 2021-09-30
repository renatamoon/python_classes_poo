#getter and setters
#setter - configurando um valor - é uma funcao que vai configurar o valor de determinar coisa
#getter - funcao que irá retornar/obter o valor que configuramos no setter

class Pessoa:

    def __init__(self):
        self.atributo = 'inicial'

    @property #quer que essa funcao quer que se comporte como um atributo
    def nome(self):
        return "Otavio Miranda"

    @nome.setter #recebe um valor para configurar
    def nome(self, nome):
        self.atributo = nome

p1 = Pessoa()
print(p1.atributo)
print(p1.nome)





