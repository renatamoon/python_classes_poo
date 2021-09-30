#atributos de classes

class A:
    vc = 123 #variavel de classe

a1 = A()
a2 = A()

A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)