from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones=0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones=Raton.contador_ratones+1
        self.__idRaton=Raton.contador_ratones
    def __str__(self):
        return "ID RATON:"+str(self.__idRaton)+" |Marca:"+self._marca+" |Tipo entrada: "+self._tipo_entrada

raton1=Raton("USB","HP")
#print(raton1)
raton2=Raton("USB","ACER")
#print(raton2)
raton3=Raton("Bluetooth","GAMER")