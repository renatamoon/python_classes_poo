import os

caminho_procura = input('DIGITE UM CAMINHO: ')
termo_procura = input('DIGITE UM TERMO PARA PROCURA: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')

conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura): #listas
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print(arquivo)

                print()
                print("ENCONTREI O ARQUIVO: ", arquivo)
                print("CAMINHO: ", caminho_completo)
                print("NOME: ", nome_arquivo)
                print("EXTENSÃO: ", ext_arquivo)
                print("TAMANHO: ", tamanho)
                print('TAMANHO FORMATADO: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print("SEM PERMISSÃO")
            except FileNotFoundError as e:
                print("ARQUIVO NÃO ENCONTRADO")
            except Exception as e:
                print("ERRO DESCONHECIDO", e)

print()
print(f'{conta} arquivo(s) encontrado(s)')