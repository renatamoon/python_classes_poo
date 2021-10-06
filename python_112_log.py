#tem um arquivo de log que foi gerado para mostear todos os logs

class LogMixin: #adiciona outras funcionalidades a outras classes
    @staticmethod
    def write(msg): #abrir um arquivo e escrever
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n') #QUEBRA DE LINHA

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

