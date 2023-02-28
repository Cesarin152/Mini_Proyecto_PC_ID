from Computadora import *
class Ordenes:
    contador_ordenes=0
    def __init__(self,computadoras):
        Ordenes.contador_ordenes=Ordenes.contador_ordenes+1
        self.__computadoras=computadoras
        self.__idOrden=Ordenes.contador_ordenes
    @property
    def computadoras(self):
        return self.__computadoras
    @computadoras.setter
    def computadoras(self,computadoras_nuevas):
        self.__computadoras=computadoras_nuevas
    def agregar_computadora(self,PC):
        self.__computadoras.append(PC)
    def __str__(self):
        strPC=""
        for pc in self.__computadoras:
            strPC=strPC+pc.__str__()+"\n"
        return "ORDEN:"+str(self.__idOrden)+" COMPUTADORAS:"+"\n  "+strPC
LISTAPC1=[computadora1,computadora2]
orden1=Ordenes(LISTAPC1)
print(orden1)
LISTAPC2=[computadora3,computadora1]
orden2=Ordenes(LISTAPC2)
print(orden2)