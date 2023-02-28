class Monitor:
    contador_monitor=0
    def __init__(self,marca,tamanio):
        Monitor.contador_monitor=Monitor.contador_monitor+1
        self.__idMonitor=Monitor.contador_monitor
        self.__marca=marca
        self.__tamanio=tamanio
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca_nueva):
        self.__marca=marca_nueva
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self,tamanio_nuevo):
        self.__tamanio=tamanio_nuevo
    def __str__(self):
        return "ID MONITOR:"+str(self.__idMonitor)+" |MARCA:"+self.__marca+" |TAMANIO:"+self.__tamanio
monitor1=Monitor("HP","16 PULGADAS")
#print(monitor1)
monitor2=Monitor("ACER","18 PULGADAS")
#print(monitor2)
monitor3=Monitor("GAMER","45 PULGADAS")