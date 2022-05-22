#Clase de las transiciones entre los estados
class Transicion:
    def __init__(self,origen,simbolo,destino):
        self.origen = origen
        self.simbolo = simbolo
        self.destino = destino

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getSimbolo(self):
        return self.simbolo

    def setOrigen(self,origenN):
        self.origen = origenN

    def setDestino(self,destinoN):
        self.destino = destinoN

    def setSimbolo(self,simboloN):
        self.simbolo = simboloN



