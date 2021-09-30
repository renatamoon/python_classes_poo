#ASSOCIAÇÃO DE CLASSES - é necessário que um
"""
Pessoa                          Endereço
-------                         --------
Nome                            rua
idade       ------------------  numero
sexo                            complemente
endereço                        cep
-------                         ---------
exibir_dados()                  exibir_dados()

"""
#EXEMPLO 2 - ASSOCIAÇÃO

'''
Cachorro
-nome
-idade
-proprietario

Pessoa
-nome
-sobrenome

**A associação será feita pelo "proprietario" que será o objeto
'''
class Cachorro:
    def __init__(self, nome, idade, proprietario):
        self.nome = nome
        self.idade = idade
        self.proprietario = proprietario

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

#so terá associação quando for vinculada em um objeto, ela não e feita
#nas classes

#programa principal

pessoa1 = Pessoa('Renata', 'Monteiro')
#pessoa2 = Pessoa('Luiz', 'Miranda')

cachorro1 = Cachorro('Spock', 5, pessoa1) #aqui que se fez a associação
#pois estou colocando o objeto pessoa1 como atributo na var cachorro

print('Nome do Cachorro: ', cachorro1.nome)
print('Proprietário: ', cachorro1.proprietario.nome)

#execute:
# Nome do Cachorro:  Spock
# Proprietário:  Renata















