#METODOS MAGICOS

class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste
        # def haha(*args, **kwargs):
        #     print("Fala Oi")
        # cls.haha = haha

        #return object.__new__(cls)

    def __str__(self):
        return 'Essa é a classe A criada para tal coisa'

    def __del__(self):
        print('objeto coletado.')

    def __call__(self, *args, **kwargs): #faz a classe se comportar como uma funcao
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

        # print(args)
        # print(kwargs)

    def __init__(self):
        print('EU SOU O INIT')

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'você nao pode fazer isso'
        else:
            self.__dict__[key] = value


a = A()
variavel = a(1,2,4,5,6,7,8,9,10)
print(variavel)
a.nome = 'Luiz Otavio'
print(a.nome)
a.qualquer = 225
print(a.nome, a.qualquer)
print(a)
# a(1,2,3,4,5, nome='Luiz')
#a.haha()
# b = A()
# c = A()

#print(id(a), id(b), id(c)) #todas sao o mesmo objeto