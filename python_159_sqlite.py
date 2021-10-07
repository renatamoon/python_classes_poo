import sqlite3
#criando os objetos
conexao = sqlite3.connect('basededados.db')
#executa os comandos dentro da base de dados que criamos
cursor = conexao.cursor()

#---------------------INCLUSAO de dados da tabela

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
# #inserindo um registro na tabela
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#             {'nome': 'Joãozinho', 'peso': 25}
#             )
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#             {'id': None, 'nome': 'Daniel', 'peso': 80}
#             )
# #executar programa
# conexao.commit()

#---------------------alteração de dados da tabela

# cursor.execute(
            #AQUI DA UM UPDATE NA BASE DE DADOS
            # 'UPDATE clientes SET nome=:nome WHERE id=:id',
            # {'nome': 'Joana', 'id': 2}

        #---------DA UM DELETE NA BASE DE DADOS
        # 'DELETE FROM clientes WHERE id=:id',
        # {'id': 2}
# )
# conexao.commit()

#mostrar todos os valores dentro da tabela
# cursor.execute('SELECT * FROM clientes')
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 50})

for linha in cursor.fetchall(): #buscar os valores dentro da table
    nome, peso = linha #desempacotando
    #print(linha) #sairá uma tupla com os valores
    print(nome, peso)

#programa principal
cursor.close()
conexao.close()