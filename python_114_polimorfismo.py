#polimorfismo = permite que classes derivadas de uma mesma superclasse tenham metodos iguais
#mas comportamentos diferentes


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(ABC):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(ABC):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('Um assunto')
c.fala('Outro assunto')
