import os
import shutil

caminho_original = 'Office\Desktop\media_total\media2'
caminho_novo = 'Office\Desktop\media_total\medias'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe!')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if 'txt' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso!')


