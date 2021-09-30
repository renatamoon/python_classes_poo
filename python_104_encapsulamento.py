#104 - encapsulamento
"""
public, protected, private

*para que um atributo seja publico, somente escrever o atributo normal
*para que um atributo seja protected, coloca "_" um underline (mas ele é publico ainda, so tem 1 underline)
*para que um atributo seja private, coloca "__" dois underlines

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property #quando usamos esse decorador, queremos obter um dado
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados: #se essa chave clientes nao estiver
            #neste dicionario, tem que criar a chave clientes - recebendo ID e nome
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            #vai atualizar os dados do clientes dentro da chave

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'] [id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.__dados ='Outra coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados)
print(bd.dados)

#bd.apaga_clientes(2) #no caso so recebe o id do cliente apra apagar
# bd.lista_clientes()
# bd.dados = 'uma outra coisa'

#no caso apagou o MIranda, e deixou o cliente 1 e 3
# print(bd.dados) #execute: {'clientes': {1: 'Otavio', 2: 'Miranda', 3: 'Rose'}}
















