from datetime import datetime

class Pessoa: #quando uma funcao esta dentro de uma classe
    #ela é um metodo
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #var da classe
    #todos os objetos terão essa variavel
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

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade #para usar a variavel ano_atual que está
    #fora da classe, tem que usar o self pra chamar como usamos acima

# ---------------- não precisa estar em files diferentes

p1 = Pessoa('Luiz', 29) #usando o modulo para criar uma pessoa
#p2 = Pessoa('Joao', 32) #usando o modulo para criar outra pessoa
#todas as instancias devem ter esses parametros padrao
p2 = Pessoa('Joao', 32)

# print(p1.ano_atual)
# print(p2.ano_atual)

#print(Pessoa.ano_atual) #usando a classe em si, usando a var da classe

print(p1.get_ano_nascimento()) #usando o valor da idade de p1 e pegando o ano de nascimento
print(p2.get_ano_nascimento())

p1.comer('maça')
p1.comer('maça')
p1.falar('assunto')
p1.parar_falar()
p1.comer('massa')