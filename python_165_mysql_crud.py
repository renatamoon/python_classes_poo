import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user = 'root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('**CONEXÃO FECHADA***')
        conexao.close()

#-------------INSERIR VALORES NA BASE DE DADOS ISAMD um insert normal e uma lista

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES '\
#         '(%s, %s, %s, %s)'
# #
#         dados = [
#                 ('MURIEL', 'FIGUEIREDO', 19, 55),
#                 ('CARLA', 'FIGUEIREDO', 19, 55),
#                 ('LILITH', 'MARONE', 19, 55),
#          ]
#         cursor.executemany(sql, dados)
#         conexao.commit()


#------DELETANDO OS VALORES DE UMA LISTA
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'

        cursor.execute(sql, (6,))
        conexao.commit() """

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#
#         cursor.execute(sql, (7,8,9))
#         conexao.commit()

# with conecta() as conexao:
#      with conexao.cursor() as cursor:
#          sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#
#          cursor.execute(sql, (10, 12))
#          conexao.commit()

#--------------------CONSULTA DE VALORES - CRUDE - CREATE READ UPDATED AND DELETE

with conecta() as conexao:
      with conexao.cursor() as cursor:
          sql = 'UPDATE clientes SET name=%s WHERE id=%s'
          cursor.execute(sql, ('JOANA', 5))
          conexao.commit()

#-------------ADICIONANDO LIMITE NA CONSULTA
#GERENCIADOR DE CONTEXTO

with conecta() as conexao: #FECHANDO A CONEXAO
    with conexao.cursor() as cursor:  #FECHANDO O CURSOR
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')  #dando limite as consultas usando LIMIT AS
        #Pedindo para ordenar by ID DESC ou ASC de maneira decrescente, crescente
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

#-------------OUTRA FORMA DE CONSULTA
"""
with conexao.cursor() as cursor:
    cursor.execute('SELECT nome as n, sobrenome as sn FROM clientes')
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha['n'], linha['sn']) #apelidadndo o nome e sobrenome
        #não é uma boa pratica de programacao
"""
#-------------selecionar os nomes
"""
with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha['nome'], linha['sobrenome']) #mostrar somente dados nome e sobrenome
"""
