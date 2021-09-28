class Pessoa: #quando uma funcao esta dentro de uma classe
    #ela é um metodo
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome #mesmo que o valor da self seja igual ao
        #parametro da funcao, eles nao sao iguais, pois um recebe o valor do outro
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        #variavel = 'Valor'
        #print(variavel) #somente podemos usar o valor dessa variavel dentro
        #dessa classe, nao podemos usa-la fora

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} ja esta falando')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao está comendo ...')
            return

        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return ano_atual = self.idade
        pass