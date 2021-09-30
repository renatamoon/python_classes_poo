#PRMEIRA AULA DE POO
#CRIAR UMA CLASSE PESSOA
#ATRIBUTOS: NOME, EMAIL, TELEFONE
#METODOS: UM METODO PARA EXIBIR OS DADOS DESTA PESSOA

'''caso nao seja dado os paramentros de entrada do construtor, não podemos informar-lis
quando criar o objeto pessoa1 ou pessoa2'''

class Pessoa:
    def __init__(self, nome, email, telefone): #construtor + parametros de entrada
        #atributos
        self.nome = nome #tem que inicializar as variaveis
        self.email = email
        self.telefone = telefone
        #no caso a variavel nome vai ser inclusa no .nome do self do objeto Pessoa
        '''quando tem um self, estamos dizendo que o .nome é um atributo do self
        que é o Objeto Pessoa. Entao self é Pessoa'''

    #metodo exibir dados
    def exibir_dados(self):
        print("=-"*10)
        print("Nome: ", self.nome)
        print("Email: ", self.email)
        print("Email: ", self.telefone)

        #vai exibir os dados pra qualquer pessoa, pois estou usando o self.nome, self.email
        #ou seja, nao importa se é pessoal1 ou pessoa2, ele sempre irá atribuir para qualquer
        #pessoa
pessoa1 = Pessoa('Renata', 'r_cardoso@email.com', 34620392)
pessoa2 = Pessoa('maria', 'maria@gmail.com', 11976741274)

pessoa1.exibir_dados()
pessoa2.exibir_dados()

print("=-"*10)

"""
#programa principal

pessoa1 = Pessoa('Renata', 'r_cardoso@email.com', 34620392) #esses valores que estou mandadno
#aqui pro pessoa1, são os valores que vou mandar pro objeto Pessoa
#toda vez que vamos criar atributos, ele sempre colocará dentro de cada um dos
#atributos do init
pessoa2 = Pessoa('maria', 'maria@gmail.com', 11976741274)

pessoa1.email = "Renata_monteiro@gmail.com" #mudando um atributo já informado
#quando ele printar, já mostra o email informado por ultimo

#pessoa1 dados:
print("Nome: ", pessoa1.nome, "Email: ", pessoa1.email) #imprimindo os atributos do objeto pessoa1

#pessoa2 dados:
print("Nome: ", pessoa2.nome, "Email: ", pessoa2.email) """

nome = input("INFORME O NOME: ")
email = input("INFORME O EMAIL: ")
telefone = int(input("INFORME O TELEFONE: "))

pessoa3 = Pessoa(nome, email, telefone) #criar o objeto - informar as variaveis
#que foram recebidas no imput e que vão ser armazenadas os valores
pessoa3.exibir_dados() #mostrar os dados informados para o usuário

