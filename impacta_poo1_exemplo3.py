#classe TRIANGULO
#atributos - lado_a, lado_b, lado_c
#metodos = Calcular o perimetro - soma dos 3 lados
#pedir que o usuario informe as medidas dos lados
#criar o objeto com essas medidas
"""
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

a = float(input("DIGITE O VALOR DO LADO A: "))
b = float(input("DIGITE O VALOR DO LADO B: "))
c = float(input("DIGITE O VALOR DO LADO C: "))

triangulo1 = Triangulo(a, b, c)

print(f'O perimetro total dos lados inseridos é: ', triangulo1.calcular_perimetro())
"""
#-----ou podemos fazer essa seguinte:

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

lista = []

for i in range(1): #repetirá uma vez
    a = float(input("Digite o primeiro lado: "))
    b = float(input("Digite o segundo lado: "))
    c = float(input("Digite o terceiro lado: "))
    triangulo1 = Triangulo(a, b, c)
    lista.append(triangulo1)

for n in lista:
    print(n.calcular_perimetro())


