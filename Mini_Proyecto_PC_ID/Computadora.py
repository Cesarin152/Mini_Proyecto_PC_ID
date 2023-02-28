from Raton import *
from Teclado import *
from Monitor import *
class Computadora:
    contador_computadora=0
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora=Computadora.contador_computadora+1
        self.__idComputadora=Computadora.contador_computadora
        self.__nombre=nombre
        self.__monitor=monitor
        self.__teclado=teclado
        self.__raton=raton
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre_nuevo):
        self.__nombre=nombre_nuevo
    @property
    def monitor(self):
        return self.__monitor
    @monitor.setter
    def monitor(self,monitor_nuevo):
        self.__monitor=monitor_nuevo
    @property
    def teclado(self):
        return self.__teclado
    @teclado.setter
    def teclado(self,teclado_nuevo):
        self.__teclado=teclado_nuevo
    @property
    def raton(self):
        return self.__raton
    @raton.setter
    def raton(self,raton_nuevo):
        self.__raton=raton_nuevo
    def __str__(self):
        return self.__nombre+":"+str(self.__idComputadora)+"\n  "+self.__monitor.__str__()+"\n  "+self.__teclado.__str__()+"\n  "+self.__raton.__str__()
computadora1=Computadora("HP",monitor1,Teclado1,raton1)
#print(computadora1)
computadora2=Computadora("ACER",monitor2,Teclado2,raton2)
#print(computadora2)
computadora3=Computadora("GAMER",monitor3,Teclado3,raton3)