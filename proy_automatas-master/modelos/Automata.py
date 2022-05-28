from modelos.Estado import *
from modelos.Transicion import *


class Automata:
    def __init__(self, alf, ini, fin):
        self._estados = []  # objetos
        self._alfabeto = []
        self._estado_inicial = []
        self._estados_finales = []
        self.listaTransiciones = []  # lista de transiciones entre los estados del automata

    def agregarEstado(self, nuevoEstado):
        nuevo = Estado(nuevoEstado)
        self._estados.append(nuevo)

    def setEstadoInicial(self, estado):
        for est in self._estados:
            if est.getNombre() == estado:
                est.cambiarEstadoInicial()

    def setEstadosFinales(self, estados):
        for estado in estados:
            for est in self._estados:
                if estado == est.getNombre():
                    est.cambiarEstadoFinal()

    def eliminarEstado(self, nombreEstado):
        for estado in self._estados:
            if nombreEstado == estado.getNombre():
                self._estados.remove(estado)

    def getEstados(self):
        return self._estados

    def getEstadoInicial(self):
        for estado in self._estados:
            if estado.esEstadoInicial():
                return estado.getNombre()

    def getEstadosFinales(self):
        res = []
        for estado in self._estados:
            if estado.esEstadoFinal():
                res.append(estado)
        return res

    # Obtener lista de transiciones del automata
    def getTransiciones(self):
        return self.listaTransiciones

    def setTransiciones(self, transicion):
        self.listaTransiciones = transicion

    # Obtener estado
    def obtenerEstado(self, estadoB):
        for estado in self._estados:
            if estado.getNombre() == estadoB:
                return estado
        print("El estado no existe")

    # Verificar si estadp existe en la lista de estados del automata
    def verificarEstado(self, estadoV):
        for estado in self._estados:
            if estadoV == estado.getNombre():
                return True
        return False

        # Agregar Transicion

    def agregarTransicion(self, origen, simbolo, destino):
        if self.verificarEstado(origen) and self.verificarEstado(destino):  # Verificamos que origen y destino existan
            if not self.buscarTransicion(origen, destino, simbolo):  # Si la transicion no existe
                self.listaTransiciones.append(
                    Transicion(origen, simbolo, destino))  # Agregamos la transicion  a la lista de transiciones
                self.obtenerEstado(origen).getListaAdyacentes().append(destino)  # Agregamos la conexion al estado
            else:
                print("La transicion ya existe")
        else:
            print("Algun vertice no existe")

            # Buscar Transicion

    def buscarTransicion(self, origen, destino, simbolo):
        for transicion in self.listaTransiciones:
            if transicion.getOrigen() == origen and transicion.getDestino() == destino and transicion.getSimbolo() == simbolo:
                return True  # si la transicion es encontrada se envia un True
        return False  # si la transicion no es encontrada enviamos False

    # Imprimir transiciones
    def imprimirTransiciones(self):
        for transiciones in self.listaTransiciones:
            print("Transicion: ", transiciones.getOrigen(), " - ", transiciones.getDestino(),
                  " simbolo: ", transiciones.getSimbolo())

    # Imprimir Estados
    def imprimirEstados(self):
        for estado in self._estados:
            print("Estado: ", estado.getNombre())
            print("Conexiones: ", estado.getListaAdyacentes())
