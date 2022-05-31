import sys  # control del sistema
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import json
import os
from graphviz import Digraph
from modelos.Automata import Automata
from control.Operaciones import Operaciones
from modelos.Estado import Estado
from modelos.Transicion import Transicion

# pip install tkinter, graphviz

os.environ["PATH"] += os.pathsep + 'C:/Users/Luis/Documents/GRAPHVIZ/bin/'  # esta ruta cambia segun el computador :v
listaAutomatas = []


def dibujarAutomata(automatas):
    imagen = Digraph(format='png')

    cont = 1

    for automata in automatas:
        imagen.node(str(cont), style='invisible')
        automata.imprimirEstados()
        for estado in automata.getEstados():
            if estado.getNombre() is automata.getEstadoInicial():
                if estado in automata.getEstadosFinales():
                    imagen.node(str(estado.getNombre()), root='true', shape='doublecircle')
                else:
                    imagen.node(str(estado.getNombre()), root='true')
                imagen.edge(str(cont), str(estado.getNombre()), style='bold')

            elif estado in automata.getEstadosFinales():
                imagen.node(str(estado.getNombre()), shape='doublecircle')
            else:
                imagen.node(str(estado.getNombre()))

        for transicion in automata.getTransiciones():
            imagen.edge(str(transicion.getOrigen()), str(transicion.getDestino()), label=transicion.getSimbolo())
        cont += 1

    imagen.render('src/automatas')


def actualizarImagenes(automatas):
    dibujarAutomata(automatas)
    ImagenAutomatas.configure(file="src/automatas.png")
    labelImagen.configure(image=ImagenAutomatas)

    ImagenResultado.configure(file="src/resultado.png")
    labelImagenR.configure(image=ImagenResultado)


def union():
    print("------------------Union ------------------------------")
    a1aux = automata1.get()
    a2aux = automata2.get()
    try:
        a1aux = int(a1aux)
        a2aux = int(a2aux)

        a1 = listaAutomatas[a1aux]
        a2 = listaAutomatas[a2aux]

        op = Operaciones(a1, a2)

        listaRes = op.union_inicial()
        estados_de_aceptacion = aux1.getEstadosFinales()

        # Buscamos el estado inicial
        estado_inicial = listaRes[0][0]
        print("Estado inicial ", estado_inicial)

        estados_finales = []

        for automata in listaAutomatas:
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

        automata_resultante2 = op.unionFinal(estado_inicial, listaRes, listaAutomatas, estados_finales)
        print("Automata resultante exitosamente! ", automata_resultante2)

        automata_resultante2.dibujarAutomata()
        actualizarImagenes(listaAutomatas)
        tkinter.messagebox.showwarning(message="Operacion Exitosa", title="Exito")
    except ValueError:
        tkinter.messagebox.showwarning(message="Please, enter correct values", title="Error")


def interseccion():
    print("------------------Interseccion ------------------------------")
    a1aux = automata1.get()
    a2aux = automata2.get()
    try:
        a1aux = int(a1aux)
        a2aux = int(a2aux)

        a1 = listaAutomatas[a1aux]
        a2 = listaAutomatas[a2aux]

        op = Operaciones(a1, a2)

        listaRes = op.interseccion_inicial()

        # Buscamos el estado inicial
        estado_inicial = listaRes[0][0]
        print("Estado inicial ", estado_inicial)

        estados_de_aceptacion = []

        for automata in listaAutomatas:
            estados_de_aceptacion.append(automata.getEstadosFinales())

        estados_finales = ""
        for estado_x_automata in estados_de_aceptacion:
            for estado in estado_x_automata:
                if estado.getNombre() not in estados_finales:
                    estados_finales += estado.getNombre()

        print(lista_automatas)
        automata_resultante = op.interseccion_final(estado_inicial, listaRes, listaAutomatas, [estados_finales])
        print("Automata resultante exitosamente! ", automata_resultante)

        automata_resultante.imprimirEstados()
        automata_resultante.imprimirTransiciones()
        automata_resultante.dibujarAutomata()
        actualizarImagenes(listaAutomatas)
        tkinter.messagebox.showwarning(message="Operacion Exitosa", title="Exito")
    except ValueError:
        tkinter.messagebox.showwarning(message="Please, enter correct values", title="Error")


def complemento():
    aux = automata.get()
    a1aux = automata1.get()

    try:
        aux = int(aux)
        a1aux = int(a1aux)

        a = listaAutomatas[aux]
        a2 = listaAutomatas[a1aux]

        op = Operaciones(a, a2)

        automata_resultante = op.complemento(a)

        automata_resultante.dibujarAutomata()
        actualizarImagenes(listaAutomatas)
        tkinter.messagebox.showwarning(message="Operacion Exitosa", title="Exito")
    except ValueError:
        tkinter.messagebox.showwarning(message="Please, enter correct values", title="Error")


def reverso():
    aux = automata.get()
    a1aux = automata1.get()

    try:
        aux = int(aux)
        a1aux = int(a1aux)

        a = listaAutomatas[aux]
        a2 = listaAutomatas[a1aux]

        op = Operaciones(a, a2)

        automata_resultante = op.reverso(a)

        automata_resultante.dibujarAutomata()

        actualizarImagenes(listaAutomatas)
        tkinter.messagebox.showwarning(message="Operacion Exitosa", title="Exito")
    except ValueError:
        tkinter.messagebox.showwarning(message="Please, enter correct values", title="Error")


def completar():
    aux = automata.get()
    a1aux = automata1.get()

    try:
        aux = int(aux)
        a1aux = int(a1aux)

        a = listaAutomatas[aux]
        a2 = listaAutomatas[a1aux]

        op = Operaciones(a, a2)

        if a.esCompleto():
            print("Es completo")
            tkinter.messagebox.showwarning(message="El automata es completo", title="Error")
        else:
            print("No es completo")
            op.completar(a)
            a.imprimirTransiciones()

        a.dibujarAutomata()

        actualizarImagenes(listaAutomatas)
        tkinter.messagebox.showwarning(message="Operacion Exitosa", title="Exito")
    except ValueError:
        tkinter.messagebox.showwarning(message="Please, enter correct values", title="Error")


main = Tk()

main.geometry("1300x700")
main.title("Proyecto Autómatas 2022")
main.resizable(0, 0)
main.iconbitmap("src/Icono.ico")
main.config(bg="gray")

topFrame = Frame(main)
topFrame.pack()
topFrame.config(bg="blue", width="1100", height="75", relief="ridge", bd="4")
Label(topFrame, text="Proyecto Autómatas 2022", fg="white", bg="blue", font=("Comic Sans MS", 18)).place(x="375",
                                                                                                         y="10")

automata1 = Entry(main)
automata2 = Entry(main)
automata = Entry(main)

Label(main, text="ID autómata 1", font=("Arial", 15), bg="gray").place(x="15", y="100")
automata1.place(x=15, y=130)
Label(main, text="ID autómata 2", font=("Arial", 15), bg="gray").place(x="15", y="155")
automata2.place(x=15, y=185)
Label(main, text="ID automata", font=("Arial", 15), bg="gray").place(x="445", y="100")
automata.place(x=445, y=130)

Label(main, text="Todos los automatas", font=("Arial", 15), bg="gray", fg="white").place(x="15", y="210")
Label(main, text="Resultado", font=("Arial", 15), bg="gray", fg="white").place(x="735", y="210")

Button(main, text="Unión", command=union, font=("Arial", 15), width=10).place(x="210", y="115")
Button(main, text="Intersección", command=interseccion, font=("Arial", 15), width=10).place(x="210", y="170")
Button(main, text="Complemento", command=complemento, font=("Arial", 15), width=12).place(x="640", y="115")
Button(main, text="Reverso", command=reverso, font=("Arial", 15), width=12).place(x="640", y="170")
Button(main, text="Completar Automata", command=completar, font=("Arial", 15)).place(x="800", y="115")

main.fileName = tkinter.filedialog.askopenfilename(filetypes=(("json files", "*.json"), ("all files", "*.*")))

try:
    with open(main.fileName) as file:
        automatas = json.load(file)
        listaAutomatas = []

        lista_automatas = automatas["automatas"]
        cont = 0
        print(len(lista_automatas))
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
            cont = cont + 1
            print("------------------------------------------")

            listaAutomatas.append(aux1)

        dibujarAutomata(listaAutomatas)

        ImagenAutomatas = PhotoImage(file="src/automatas.png")
        labelImagen = Label(main, image=ImagenAutomatas, width=550, height=450)
        labelImagen.place(x="15", y="235")

        ImagenResultado = PhotoImage(file="src/resultado.png")
        labelImagenR = Label(main, width=550, height=450)
        labelImagenR.place(x="735", y="235")


except:
    tkinter.messagebox.showwarning(
        message="El archivo seleccionado no cumple con los datos necesarios para ejecutar el programa", title="Error")
    print("El archivo seleccionado no cumple con los datos necesarios para ejecutar el programa")
    main.destroy()

main.mainloop()
