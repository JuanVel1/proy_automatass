from modelos.Estado import *
from modelos.Transicion import *
import os
from graphviz import Digraph

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'


class Automata:
    def __init__(self, alf, ini, fin):
        self._estados = []  # objetos
        self._alfabeto = alf
        self._estado_inicial = ini
        self._estados_finales = fin
        self.listaTransiciones = []  # lista de transiciones entre los estados del automata
        self.imagen = Digraph(format='png')

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

    def getAlfabeto(self):
        return self._alfabeto

    def getEstadoInicial(self):
        """for estado in self._estados:
            if estado.esEstadoInicial():
                """
        return self._estado_inicial

    def getEstadosFinales(self):
        res = []
        for estado in self._estados:
            if estado.esEstadoFinal():
                res.append(estado)
        return res

    # Obtener lista de transiciones del automata
    def getTransiciones(self):
        return self.listaTransiciones

    def setTransiciones(self, transiciones):
        self.listaTransiciones = transiciones

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
                aux = self.obtenerEstado(origen).getListaAdyacentes()
                aux.append(destino)
                self.obtenerEstado(origen).setListaAdyacentes(aux)
                # Agregamos la conexion al estado
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

    def eliminarTransicion(self, estado):
        if self.verificarEstado(estado.getNombre()):
            for transicion in self.listaTransiciones:
                if transicion.getOrigen() == estado.getNombre() or transicion.getDestino() == estado.getNombre():
                    self.listaTransiciones.remove(transicion)
        else:
            print("Estado inexistente")

        # Imprimir transiciones

    def imprimirTransiciones(self):
        print("------------------Transiciones ------------------------------")
        for transiciones in self.listaTransiciones:
            print("Transicion: ", transiciones.getOrigen(), " - ", transiciones.getDestino(), " - ",
                  " simbolo: ", transiciones.getSimbolo())

        # Imprimir Estados

    def imprimirEstados(self):
        print("------------------Estados ------------------------------")
        for estado in self._estados:
            print("Estado: ", estado.getNombre())
            print("Conexiones: ", estado.getListaAdyacentes())
            if estado.esEstadoFinal():
                print("Es estado final")
            if estado.esEstadoInicial():
                print("Es estado inicial")
            print("..")
        print("------------------ ------------------------------")

    # Desactivar estado inicial para reverso
    def desactivarInicial(self):
        self._estado_inicial = None
        for estado in self._estados:
            if estado.esEstadoInicial():
                estado.cambiarEstadoInicial()

    def esCompleto(self):
        esta = True
        for simbolo in self.getAlfabeto():
            for estado in self.getEstados():
                simbolos_x_estado = []
                for transicion in self.getTransiciones():
                    if transicion.getOrigen() == estado.getNombre() or transicion.getDestino() == estado.getNombre():
                        simbolos_x_estado.append(transicion.getSimbolo())
                if simbolo not in simbolos_x_estado:
                    esta = False
                    return esta
        return esta

    def dibujarAutomata(self):
        self.imagen.clear(keep_attrs=True)
        self.imagen.node('fake', style='invisible')

        for estado in self._estados:
            if estado.getNombre() is self._estado_inicial:
                if estado.getNombre() in self._estados_finales:
                    self.imagen.node(str(estado.getNombre()), root='true', shape='doublecircle')
                else:
                    self.imagen.node(str(estado.getNombre()), root='true')
                self.imagen.edge('fake', str(estado.getNombre()), style='bold')

            elif estado.getNombre() in self._estados_finales:
                self.imagen.node(str(estado.getNombre()), shape='doublecircle')
            else:
                self.imagen.node(str(estado.getNombre()))

        for transicion in self.listaTransiciones:
            self.imagen.edge(str(transicion.getOrigen()), str(transicion.getDestino()),
                             label=transicion.getSimbolo())

        self.imagen.render("src/resultado")
