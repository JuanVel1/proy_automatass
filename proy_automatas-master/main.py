import sys  # control del sistema
import pygame  # interfaz grafica
from modelos.Automata import Automata

# CTRL + ALT + L --> FORMAT
pygame.init()
ancho, alto = 1100, 700
pygame.display.set_caption("Proyecto automatas 2022")
clock = pygame.time.Clock()  # reloj para controlar la velocidad de ejecucion del programa
pantalla = pygame.display.set_mode((ancho, alto))
autm = Automata()



# Se ingresa al ciclo de pygame
while True:
    for event in pygame.event.get():


        # Si se sale de la equis se sale del sys
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    clock.tick(30)