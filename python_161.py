import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone): #ou insere ou ignora caso ouver algum erro
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Luiz', '111111')
    # agenda.inserir('Maria', '222222')
    # agenda.inserir('Vania', '125845')
    # agenda.inserir('Luiza', '125475')
    # agenda.inserir('Lucas', '113289')
    #agenda.editar('Francisco', '125485', 3)
    agenda.inserir('Luiz Otavio', '122555')
    agenda.inserir('Luiz Felipe', '854455')
    agenda.inserir('Luiz Janio', '124585')
    agenda.inserir('Mario Luiz Antonio', '124585')
    # agenda.excluir(3)
    # agenda.listar()
    agenda.buscar('Luiz') #buscar todos os nomes que tem luiz