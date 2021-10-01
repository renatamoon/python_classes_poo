#AGREGAÇÃO
#uma classe usa uma classe, mas ela precisa dessa classe, não consegue funcionar sem ela

class CarrinhoDeCompras:
    #essa classe pode existir sozinha, mas ela precisa da Classe Produto
    def __init__(self):
        self.produtos = [] #recebe uma lista vazia

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
#ela pode existir sozinha, ela nao depende da classe Carrinho de compraS
#POREM a classe Carrinho de compras depende da classe produto
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

#programa principal

carrinho = CarrinhoDeCompras()

produto1 = Produto('camiseta', 50)
produto2 = Produto('lapis', 2.5)
produto3 = Produto('caderno', 29)
produto4 = Produto('borracha', 1)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.inserir_produto(produto4)

carrinho.lista_produto()
print("O TOTAL DA COMPRA FOI: R$", carrinho.soma_total())



