#classe Livro
#não possui metodos
#criar dois objetos
#atributos: titulo, autor, quatidade_paginas

class Livro:
    def __init__(self, titulo, autor, qnt_paginas):
        self.titulo = titulo
        self.autor = autor
        self.qnt_paginas = qnt_paginas

    def exibir_dados_livro(self):
        print("O Título do Livro é: ", self.titulo)
        print("O Autor do Livro é: ", self.autor)
        print("A quantidade de páginas do Livro é: ", self.qnt_paginas)

#programa principal
livro1 = Livro('Garota Exemplar', 'Gyllian Flynn', 380)
livro2 = Livro('A Herdeira', 'Henry James', 250)

livro1.exibir_dados_livro()
print("=-"*10)
livro2.exibir_dados_livro()


