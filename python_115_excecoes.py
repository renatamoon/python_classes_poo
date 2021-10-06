#CRIANDO EXCEÇÕES
#quer criar um erro personalizado
#por convencao toda excecao termina com ERROR

class TaErradoError(Exception):
    pass

#levantando excecoes que nos mesmos criamos
def teste():
    raise TaErradoError('Errado!')

try:
    teste()
except TaErradoError as error:
    print(f'Erro: {error}')















