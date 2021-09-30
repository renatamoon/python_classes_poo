'''criar classe aluno
-atributos: ra, nome, email, lista de notas
-metodos: inserir_nota, calcular_nota
'''
class Aluno:
    def __init__(self, ra, nome, email): #nao irá receber uma lista de notas
        #porque queremos uma lista de notas vazia
        self.ra = ra
        self.nome = nome
        self.email = email
        self.lista_notas = [] #lista vazia para que sejam inseridos depois

    def inserir_nota(self, nota): #o metodo recebeu uma nota
        print("=-" * 10)
        self.lista_notas.append(nota) #inseriu a nota atraves do append dentro
        #da lista de notas, que é um atributo do objeto Aluno

    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
                #somatorio da lista de notas / tamanho da lista
        return media #retorna a variavel com a media

#programa principal
#incluindo os dados do aluno 1 e 2
aluno1 = Aluno(12354, 'Lucas', 'lucas@gmail.com')
aluno2 = Aluno(15585, 'Renato', 'renato@hotmail.com')

#incluindo as notas do aluno1
aluno1.inserir_nota(10)
aluno1.inserir_nota(8)
aluno1.inserir_nota(9)

#incluindo as notas do aluno2
aluno2.inserir_nota(8)
aluno2.inserir_nota(6)
aluno2.inserir_nota(4)

#usando o metodo de calculo de media para os dois alunos
print(f'A média do {aluno1.nome} é: ', aluno1.calcular_media())
print("=-" * 10)
print(f'A média do {aluno2.nome} é: ', aluno2.calcular_media())







