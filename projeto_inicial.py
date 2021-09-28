class Pessoa1:

    esse_ano = 2021

    def __init__(self, nome, idade, trabalhando=False, tempoLivre=False):
        self.nome = nome
        self.idade = idade
        self.trabalhando = trabalhando
        self.tempoLivre = tempoLivre

    def trabalhar(self, horario):
        if self.trabalhando:
            print(f'{self.nome} não está de lazer, pois está trabalhando')
            return

        if self.tempoLivre:
            print(f'{self.nome} está em tempo livre')
            return

        print(f'{self.nome} está trabalhando no horario {horario}')
        self.trabalhando = True


    def parar_trabalhar(self):
        if not self.trabalhando:
            print(f'{self.nome} não está trabalhando')
            return

        print(f'{self.nome} parou de trabalhar')
        self.trabalhando = False

    def lazer(self, atividade):
        if self.tempoLivre:
            print(f'{self.nome} já está em tempo Livre')
            return

        if self.trabalhando:
            print(f'{self.nome} está aproveitando seu lazer, não pode trabalhar')

        print(f'{self.nome} está em tempo livre {atividade}')
        self.tempoLivre = True

    def parar_lazer(self):
        if not self.tempoLivre:
            print(f'{self.nome} não está de tempo livre')
            return

        print(f'{self.nome} parou seu tempos livre/lazer')

    def get_por_ano_nascimento1(self):
        print(self.esse_ano - self.idade)

    @classmethod
    def por_ano_nascimento1(classe, nome, ano_nascimento):
        idade = classe.esse_ano - ano_nascimento
        return classe(nome, idade)

#-----------prints da classe
p2 = Pessoa1.por_ano_nascimento1('Renata', 1999)
print("nome: ", p2.nome , "e", "idade: ",  p2.idade)

p2.get_por_ano_nascimento1()


