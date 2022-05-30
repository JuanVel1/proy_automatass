class Estado:
    def __init__(self, nombre):
        self._nombre = nombre  # Nombre o letra
        self._esFinal = False
        self._esInicial = False
        self._listaAdyacentes = [] #estados con lo que esta conectado/tiene transicion


    def cambiarEstadoFinal(self):
        self._esFinal = not self._esFinal

    def cambiarEstadoInicial(self):
        self._esInicial = not self._esInicial

    def getNombre(self):
        return self._nombre

    def esEstadoInicial(self):
        return self._esInicial

    def esEstadoFinal(self):
        return self._esFinal

    def getListaAdyacentes(self):
        return self._listaAdyacentes

    def setListaAdyacentes(self, listaA):
        self._listaAdyacentes = listaA




