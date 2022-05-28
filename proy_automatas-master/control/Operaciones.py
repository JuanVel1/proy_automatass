from modelos.Automata import *
from modelos.Estado import *


class Operaciones:
    def __init__(self, a1, a2):
        self.a1 = a1  # objetos
        self.a2 = a2
        self.resultado = []

    def getResultado(self):
        return self.resultado

    def union_inicial(self):
        # Listamos los estados de cada automata
        lista1 = self.a1.getEstados()
        lista2 = self.a2.getEstados()

        listaRes = []

        # For para enlazar los estados de cada lista
        for inicial in lista1:
            # print(inicial.getNombre())
            aux = []
            for final in lista2:
                # print((inicial.getNombre(), final.getNombre()))
                aux.append((inicial.getNombre() + final.getNombre()))
            listaRes.append(aux)

        # Solo imprime
        """for res in listaRes:
            for tupla in res:
                print(res[0][0], " >> ", tupla)
                print("...")"""

        return listaRes

    # Metodo que se llama desde el main con la lista de estados ab, bc, ... creados
    def unionFinal(self, lista_estados, lista_automatas):
        automata_1, automata_2 = lista_automatas
        res = []  # variable que guardara el resultado final

        # Recorremos las transiciones de cada automata para encontrar coincidencias
        for transicion_aut1 in automata_1.getTransiciones():
            for transicion_aut2 in automata_2.getTransiciones():
                if transicion_aut1.getSimbolo() == transicion_aut2.getSimbolo():
                    print("coincidencia aut1 >> ", transicion_aut1.getOrigen(), transicion_aut1.getSimbolo(),
                          transicion_aut1.getDestino())
                    print("coincidencia aut2 >> ", transicion_aut2.getOrigen(), transicion_aut2.getSimbolo(),
                          transicion_aut2.getDestino())

                    for estados_x_automata in lista_estados:
                        for estado in estados_x_automata:
                            if estado[0] == transicion_aut1.getOrigen() and estado[1] == transicion_aut2.getOrigen():
                                print("El estado esta ", estado)
                                res.append(estado)
                                # Transicion(estado)
                            if estado[0] == transicion_aut1.getDestino() and estado[1] == transicion_aut2.getDestino():
                                print("Destino ", estado)
                                print("simbolo ", transicion_aut1.getSimbolo())
                                res.append(estado)
                                res.append(transicion_aut1.getSimbolo())
                                # transiciones.append((transicion_aut1.getOrigen(),))
        # Dividir la lista de 3 en 3 - origen, destino, simbolo
        res = [res[i:i + 3] for i in range(0, len(res), 3)]
        return res

    def agregarTransiciones(self):
        pass

    # Se supone que es reverso
    def cambiarSentido(self, origen, destino):
        for arista in self.listaAristas:
            if arista.getDestino() == destino and arista.getOrigen() == origen:
                arista.setOrigen(destino)
                arista.setDestino(origen)
                for vertice in self.getListaVertices():
                    if vertice.getDato() == origen:
                        vertice.getListaAdyacentes().remove(destino)
                    if vertice.getDato() == destino:
                        vertice.getListaAdyacentes().append(origen)
