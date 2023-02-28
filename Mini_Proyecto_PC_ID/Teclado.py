from DispositivoEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contador_teclado=0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclado=Teclado.contador_teclado+1
        self.__idTeclado=Teclado.contador_teclado
    def __str__(self):
        return "ID TECLADO:"+str(self.__idTeclado)+" |Marca:"+self._marca+" |Tipo entrada: "+self._tipo_entrada

Teclado1=Teclado("USB","HP")
#print(Teclado1)
Teclado2=Teclado("USB","ACER")
#print(Teclado2)
Teclado3=Teclado("Bluetooth","GAMER")