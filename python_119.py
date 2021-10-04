#METACLASSES
#sao as classes que criam outras classes

# class Meta(type): #type é uma metaclasse pra criar classes
#     def __new__(mcs, name, bases, namespace):
#         if name == 'A':
#             return type.__new__(mcs, name, bases, namespace)
#
#         if 'b_fala' not in namespace:
#             print(f'Oi, você pode criar o metodo b_fala em {name}')
#         else:
#             if not callable(namespace['b_fala'])
#                 print('b_fala precisa ser um metodo nao atributo')
#
#         return type.__new__(mcs, name, bases, namespace)
#
# class A(metaclass=Meta):
#     def fala(self):
#         self.b_fala()
#
# class B(A):
#     teste = 'Valor'
#     b_fala = 'Wow'
#
#     def b_fala(self):
#         print('OI')
#     def sei_la(self):
#         pass

#------------------

A = type(
    'A',
    (),
    {
      'attr':'Olá Mundo!'
    }
)

a = A()
print(a.attr)


