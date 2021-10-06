class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Carrinho:
    def __init__(self, cliente):
        self.produtos = []
        self.cliente = cliente

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        #aqui acesssamos a lista "produtos" acima e faz um append
        #de um produto qualquer nele

    def listar_produtos(self): #somente para listar as informações
        for produto in self.produtos: #percorre a lista de produtos no carrinho
            print("Descrição: ", produto.descricao, "Valor:", produto.valor)

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma

    def aplicar_desconto(self, porcentagem):
        valor = self.calcular_total()
        total = valor - (valor * porcentagem / 100)
        return total

cliente1 = Cliente("Renata Monteiro")

produto1 = Produto("Monitor", 2000)
produto2 = Produto("Agenda", 35)
produto3 = Produto("Bolsa", 75)

carrinho1 = Carrinho(cliente1) #associando o cliente1 no carrinho

carrinho1.adicionar_produto(produto1)#usando a associação, estou usando o metodo
#adicionar_produto para adicionar o produto 1 dentro do Carrinho1
carrinho1.adicionar_produto(produto3)
carrinho1.adicionar_produto(produto2)
carrinho1.adicionar_produto(produto2)

carrinho1.listar_produtos()

print("Total sem Desconto: R$", carrinho1.calcular_total())
print("TOTAL COM DESCONTO: R$", carrinho1.aplicar_desconto(10)) #requer que insira
#um valor para calcular o desconto

