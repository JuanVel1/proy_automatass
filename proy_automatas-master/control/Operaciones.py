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

        return listaRes

    # Metodo que se llama desde el main con la lista de estados ab, bc, ... creados
    def unionFinal(self, ini, lista_estados, lista_automatas, finales):
        automata_1, automata_2 = lista_automatas
        res = []  # variable que guardara el resultado.jpeg final

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
                                # print("El estado esta ", estado)
                                res.append(estado)
                                # Transicion(estado)
                            if estado[0] == transicion_aut1.getDestino() and estado[1] == transicion_aut2.getDestino():
                                # print("Destino ", estado)
                                # print("simbolo ", transicion_aut1.getSimbolo())
                                res.append(estado)
                                res.append(transicion_aut1.getSimbolo())
                                # transiciones.append((transicion_aut1.getOrigen(),))
        # Dividir la lista de transiciones de 3 en 3 - origen, destino, simbolo
        res = [res[i:i + 3] for i in range(0, len(res), 3)]
        # Instanciando la clase Automata
        nuevo_automata = Automata([res[0][2], res[1][2]], ini, finales)
        # Agregando estados
        for estados_x_automata in lista_estados:
            for estado in estados_x_automata:
                nuevo_automata.agregarEstado(estado)
        # Agregando transiciones
        for transicion in res:
            nuevo_automata.agregarTransicion(transicion[0], transicion[2], transicion[1])

        # Estableciendo estado inicial y final
        nuevo_automata.setEstadoInicial(ini)
        nuevo_automata.setEstadosFinales(finales)
        print("Estado inicial ", nuevo_automata.getEstadoInicial())
        for estado in nuevo_automata.getEstadosFinales():
            print("Estado Final ", estado.getNombre())

        return nuevo_automata

    def interseccion_inicial(self):
        # Listamos los estados de cada automata
        lista1 = self.a1.getEstados()
        lista2 = self.a2.getEstados()

        listaRes = []

        # For para enlazar los estados de cada lista
        for inicial in lista1:
            aux = []
            for final in lista2:
                aux.append((inicial.getNombre() + final.getNombre()))
            listaRes.append(aux)

        return listaRes

    def interseccion_final(self, ini, lista_estados, lista_automatas, finales):
        automata_1, automata_2 = lista_automatas
        res = []  # variable que guardara el resultado.jpeg final

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
                                res.append(estado)
                            if estado[0] == transicion_aut1.getDestino() and estado[1] == transicion_aut2.getDestino():
                                res.append(estado)
                                res.append(transicion_aut1.getSimbolo())
        res = [res[i:i + 3] for i in range(0, len(res), 3)]
        # Instanciando la clase Automata
        nuevo_automata = Automata([res[0][2], res[1][2]], ini, finales)
        # Agregando estados
        for estados_x_automata in lista_estados:
            for estado in estados_x_automata:
                nuevo_automata.agregarEstado(estado)
        # Agregando transiciones
        for transicion in res:
            nuevo_automata.agregarTransicion(transicion[0], transicion[2], transicion[1])

        # Estableciendo estado inicial y final
        nuevo_automata.setEstadoInicial(ini)
        nuevo_automata.setEstadosFinales(finales)
        print("Estado inicial ", nuevo_automata.getEstadoInicial())
        for estado in nuevo_automata.getEstadosFinales():
            print("Estado Final ", estado.getNombre())

        return nuevo_automata

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

    def complemento(self, automata):
        print("------------------Antes ------------------------------")
        automata.imprimirEstados()
        automata.imprimirTransiciones()
        for estado in automata.getEstados():
            estado.cambiarEstadoFinal()
        print("------------------Despues ------------------------------")
        automata.imprimirEstados()
        automata.imprimirTransiciones()
        return automata

    def reverso(self, automata):
        # Reverso de un autómata con Varios estados de aceptación
        # Cuando nuestro autómata tiene mas de un estado de aceptación debemos crear un nuevo estado, convertir ese
        # nuevo estado en uno de aceptación, todos los estados de aceptación pasan a ser estados de no aceptación y
        # creamos transiciones lambda hacia el nuevo estado.
        estados_aceptacion = automata.getEstadosFinales()

        if len(estados_aceptacion) > 1:
            # Tiene varios estados de aceptacion
            automata.agregarEstado("nuevo estado")
            nuevo_estado = automata.obtenerEstado("nuevo estado")
            nuevo_estado.cambiarEstadoFinal()

            for estado in estados_aceptacion:
                estado.cambiarEstadoFinal()  # todos los estados de aceptación pasan a ser estados de no aceptación
                # creamos transiciones lambda hacia el nuevo estado.
                automata.agregarTransicion(estado.getNombre(), "λ", nuevo_estado.getNombre())

            automata.imprimirEstados()
            automata.imprimirTransiciones()
            print("....")

            # Ahora hacemos el mismo proceso, cambiamos la orientación de las transiciones y nuestro estado de
            # aceptación pasa a ser un estado inicial y nuestro estado inicial pasa a ser estado de aceptación
            self.cambiarSentido(automata)

            for estado in automata.getEstadosFinales():
                estado.cambiarEstadoInicial()
                estado.cambiarEstadoFinal()

            estado_inicial = automata.getEstadoInicial()
            automata.obtenerEstado(estado_inicial).cambiarEstadoInicial()
            automata.obtenerEstado(estado_inicial).cambiarEstadoFinal()

            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            for estado in automata.getEstados():
                alcanzable = False
                for transicion in automata.getTransiciones():
                    if estado.esEstadoFinal() or estado.esEstadoInicial() or transicion.getDestino() == estado.getNombre():
                        alcanzable = True
                if alcanzable:
                    # print("Estado inalcanzable : ", estado.getNombre())
                    print("ok")
                else:
                    automata.eliminarTransicion(estado)

            automata.imprimirEstados()
            automata.imprimirTransiciones()
            print("....")
        else:
            # Ahora hacemos el mismo proceso, cambiamos la orientación de las transiciones y nuestro estado de
            # aceptación pasa a ser un estado inicial y nuestro estado inicial pasa a ser estado de aceptación
            self.cambiarSentido(automata)

            for estado in automata.getEstadosFinales():
                estado.cambiarEstadoInicial()
                estado.cambiarEstadoFinal()

            estado_inicial = automata.getEstadoInicial()
            automata.obtenerEstado(estado_inicial).cambiarEstadoInicial()
            automata.obtenerEstado(estado_inicial).cambiarEstadoFinal()

            automata.imprimirEstados()
            automata.imprimirTransiciones()
            print("....")
        return automata

    def cambiarSentido(self, automata):
        for transicion in automata.getTransiciones():
            origen = transicion.getOrigen()
            destino = transicion.getDestino()
            transicion.setOrigen(destino)
            transicion.setDestino(origen)
            estado_origen = automata.obtenerEstado(origen)
            estado_origen.getListaAdyacentes().remove(destino)
            estado_destino = automata.obtenerEstado(destino)
            estado_destino.getListaAdyacentes().append(origen)

    def getFaltantes(self, automata):
        faltantes = []  # [(estado, [simbolos]), (estado, [simbolos])...]

        # Recorremos cada estado
        for estado in automata.getEstados():
            # Almacenamos los simbolos faltantes de cada estado
            simbolos_x_estado = []
            simbolos_x_estado_faltantes = []
            for transicion in automata.getTransiciones():
                # Si el estado esta en la transicion como estado origen o destino entra
                if transicion.getOrigen() == estado.getNombre():
                    if type(transicion.getSimbolo()) is list:
                        for simbolo in transicion.getSimbolo():
                            simbolos_x_estado.append(simbolo)
                    else:
                        simbolos_x_estado.append(transicion.getSimbolo())

            print(estado.getNombre(), " > ", simbolos_x_estado)
            # Recorremos el alfabeto 0,1,...
            for simbolo in automata.getAlfabeto():
                if simbolo not in simbolos_x_estado:
                    simbolos_x_estado_faltantes.append(simbolo)

            if len(simbolos_x_estado_faltantes) < 1:
                print("estado completo")
            else:
                print(estado.getNombre(), " le faltan ", simbolos_x_estado_faltantes)
                faltantes.append((estado, simbolos_x_estado_faltantes))
        return faltantes

    def completar(self, automata):
        if automata.esCompleto():
            print("Automata ya completo!")
            return
        else:
            automata.agregarEstado("sumidero")

        faltantes = self.getFaltantes(automata)
        print(faltantes)
        sumidero = automata.obtenerEstado("sumidero")

        for estado in faltantes:
            if estado[0] != sumidero:
                # print(estado[0].getNombre())
                automata.agregarTransicion(estado[0].getNombre(), estado[1], "sumidero")

        automata.imprimirTransiciones()
