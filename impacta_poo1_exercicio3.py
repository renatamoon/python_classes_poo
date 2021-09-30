'''
Classe Televisao
Atributos:
-canal1 = None
-Volume = 0

Metodos:
-aumentar_volume = aumenta volume em 1 unidade
-diminiu_volume = diminiu volume em 1 unidade
-alterar_canal(canal)

'''

class Televisao:
    def __init__(self):
        self.canal1 = None
        self.volume = 0
        #quando eu coloco que o canal1 = None digo que os valores sempre começaram em None
        #e o volume se iniciará em 0, pois ai os valores mudarão depois

    def aumentar_volume(self): #não tem parametro de entrada
        self.volume += 1 #IRÁ AUMENTAR 1 VOLUME

    def dimunuir_volume(self):
        self.volume -= 1 #IRÁ DIMINIUR 1 VOLUME

    def alterar_canal(self, canal1):
        self.canal1 = canal1

#criando o objeto

tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.dimunuir_volume()
tv.alterar_canal(5) #modifico para o canal 5
tv.alterar_canal(7)

print("Volume: ", tv.volume)
print("Canal: ", tv.canal1)