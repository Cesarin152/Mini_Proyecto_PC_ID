class DispositivoEntrada:
    def __init__(self,tipo_entrada,marca):
        self._tipo_entrada=tipo_entrada
        self._marca=marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marcaNuevo):
        self._marca=marcaNuevo
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self,tipo_entradaNuevo):
        self._tipo_entrada=tipo_entradaNuevo