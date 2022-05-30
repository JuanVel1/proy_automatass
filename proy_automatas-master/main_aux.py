import json

from modelos.Automata import Automata
from control.Operaciones import Operaciones
from modelos.Estado import Estado
from modelos.Transicion import Transicion

if __name__ == "__main__":
    print("Leyendo  archivo .json-----")
    # ruta = input("Ingrese ruta de archivo : ")
    ruta = "src/archivo.json"
    archivo = open(ruta)
    automatas = json.load(archivo)
    lista_automatas_aux = []

    lista_automatas = automatas["automatas"]
    cont = 0
    for aut in lista_automatas:
        print("------------------------- -----------------")
        print("*********** Automata", cont, "************")

        print("*** Informacion general ***")
        print(aut['Q'])
        print(aut['Alf'])  # "Σ"
        print(aut['F'])
        print(aut['transiciones'])
        print("******************************************")

        print("*** Informacion especifica ***")
        aux1 = Automata(aut['Alf'], aut['Q0'], aut['F'])
        for estado in aut['Q']:
            aux1.agregarEstado(estado)
        for transicion in aut['transiciones']:
            aux1.agregarTransicion(transicion["origen"], transicion["simbolo"], transicion["destino"])
        aux1.setEstadoInicial(aut['Q0'])
        aux1.setEstadosFinales(aut['F'])

        print("------------------Estados -----------------------------------")
        aux1.imprimirEstados()
        print("------------------Estado Inicial -----------------------------------")
        print(aux1.getEstadoInicial())
        print("------------------Estados Finales -----------------------------------")
        for estado_aceptacion in aux1.getEstadosFinales():
            print(estado_aceptacion.getNombre())
        print("------------------Transiciones ------------------------------")
        aux1.imprimirTransiciones()
        lista_automatas_aux.append(aux1)
        cont = cont + 1

    print("------------------------------------------")
    print("------------------Union ------------------------------")
    ope = Operaciones(lista_automatas_aux[0], lista_automatas_aux[1])
    listaRes = ope.union_inicial()
    estados_de_aceptacion = aux1.getEstadosFinales()

    # Buscamos el estado inicial
    estado_inicial = listaRes[0][0]
    print("Estado inicial ", estado_inicial)

    estados_finales = []

    for automata in lista_automatas_aux:
        estados_de_aceptacion.append(automata.getEstadosFinales())

    for tupla in listaRes:
        for estado in tupla:
            for final in estados_de_aceptacion:
                if type(final) == Estado:
                    if (estado[0] == final.getNombre()) or (estado[1] == final.getNombre()):
                        if estado not in estados_finales:
                            estados_finales.append(estado)
                else:
                    for f in final:
                        if (estado[0] == f.getNombre()) or (estado[1] == f.getNombre()):
                            if estado not in estados_finales:
                                estados_finales.append(estado)

    # print("estados finales ", estados_finales)
    # print(listaRes, " << listaRes")
    automata_resultante2 = ope.unionFinal(estado_inicial, listaRes, lista_automatas_aux, estados_finales)
    print("Automata resultante exitosamente! ", automata_resultante2)

    print("------------------Interseccion ------------------------------")
    listaRes = ope.interseccion_inicial()

    # Buscamos el estado inicial
    estado_inicial = listaRes[0][0]
    print("Estado inicial ", estado_inicial)

    estados_finales = []
    estados_de_aceptacion = []

    for automata in lista_automatas_aux:
        estados_de_aceptacion.append(automata.getEstadosFinales())

    print(listaRes)

    estados_finales = ""
    for estado_x_automata in estados_de_aceptacion:
        for estado in estado_x_automata:
            if estado.getNombre() not in estados_finales:
                estados_finales += estado.getNombre()

    automata_resultante = ope.interseccion_final(estado_inicial, listaRes, lista_automatas_aux, [estados_finales])
    print("Automata resultante exitosamente! ", automata_resultante)

    automata_resultante.imprimirEstados()
    automata_resultante.imprimirTransiciones()

    print("------------------Complemento ------------------------------")
    automata_resultante1 = ope.complemento(lista_automatas_aux[1])

    print("------------------Reverso ------------------------------")
    automata_resultante1 = ope.reverso(automata_resultante2)

    print("------------------Completar ------------------------------")
    if automata_resultante1.esCompleto():
        print("Es completo")
    else:
        print("No es completo")
        # automata_resultante1.imprimirEstados()
        for estado in ope.completar(automata_resultante1):
            print(estado)
            print(estado[0].getNombre())
