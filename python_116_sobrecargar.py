#SOBRECARGA DE OPERADORES

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other): #self é a primeira instancia - other é o segundo objeto
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other): #menor que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other): #maior que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):  # maior que
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2

print(r3 < r1)
print(r1 == r3)
