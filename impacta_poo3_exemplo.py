class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario #atributo privado - QUER PROTEGER O SALARIO DO FUNCIONARIO - coloca o "__"

    def set_salario(self, salario): #alterar o salario do funcionario + parametro de entrada
        if salario > 0: #somente permite a alteração do salario se ele for maior que 0,
            #caso seja menor, então ele não deixa alterar o valor do salario
            self.__salario = salario
        else:
            print("O valor é inválido")

    #caso eu queira acessar o valor set_salario, necesssariamente eu preciso de get
    #GETTER

    def get_salario(self):
        return self.__salario #so assim consegue printar o salario alterado

funcionario1 = Funcionario("Paulo", 30, 2500) #objeto criado
funcionario1.nome = "Paulo Vieira"
funcionario1.idade = 31
funcionario1.set_salario(3000) #ocorre um erro - pois estamso tentando acessar e alterar um atributo
                                #privado de uma classe

funcionario2 = Funcionario("Maria", 25, 2000)
funcionario2.set_salario(250)

print("Nome: ", funcionario1.nome)
print("Salario: ", funcionario1.get_salario())

funcionario1._Funcionario__salario = 50