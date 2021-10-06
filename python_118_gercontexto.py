"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('ABRINDO O ARQUIVO')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('RETORNANDO AO ARQUIVO')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb): #SO VAI SER EXECUTADO QUANDO TIVER ALGUMA EXCECAO
        print('FECHANDO ARQUIVO')
        self.arquivo.close()
        return True

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma Coisa') #pedindo para abrir um arquivo txt e pedindo apra
    #escrever algo dentro """

#criando um gerenciador de contexto sem usar classe

from contextlib import contextmanager

@contextmanager
def abrir_arquivo(arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(arquivo, modo)
        yield arquivo

    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()

with abrir_arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('LINHA 1 \n')
    arquivo.write('LINHA 2\n')
    arquivo.write('LINHA 3\n')




