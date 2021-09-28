from python_98_classes_pessoa import Pessoa

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



