from clases.Base import Base
from clases.Controlador import Controlador
import pygame

def dibujo(ventana, colores):

    Controlador.rellenar_pantalla(ventana, colores)
    Base.sprites.draw(ventana)
    pygame.display.flip()