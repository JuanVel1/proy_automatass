import json

from modelos.Automata import Automata
from modelos.Estado import Estado
from modelos.Transicion import Transicion


if __name__ == "__main__":
    """aut = Automata()
    aut.agregarEstado("a")
    aut.agregarEstado("b")
    aut.agregarEstado("c")
    aut.agregarEstado("d")

    for estado in aut.getEstados():
        print(estado.getNombre())
    
    aut.setEstadoInicial("a")
    aut.setEstadosFinales(["b", "c"])
    aut.eliminarEstado("d")

    for estado in aut.getEstados():
        print(estado.getNombre())"""

    print("Leyendo  archivo .json-----")
    ruta = input("Ingrese ruta de archivo : ")
    archivo = open(ruta)
    automatas = json.load(archivo)
    aux = [] 
    
    lista_automatas = automatas["automatas"]
    cont = 0;
    for aut in lista_automatas:
        print("------------------------- -----------------")
        print("*********** Automata",cont, "************")

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
        
        print("------------------Estados -----------------------------------")
        aux1.imprimirEstados()
        print("------------------Transiciones ------------------------------")
        aux1.imprimirTransiciones()
        aux.append(aux1)
        cont = cont+1
        print("------------------------------------------")



    """for automata in aux:
        for estado in automata.getEstados():
            print(">> ", estado.getNombre())
        print("**********")"""
