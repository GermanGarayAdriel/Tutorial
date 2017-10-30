from archivos.nivel import *
from clases.Controlador import *

def juego(colores, mario):

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    nivel(reloj, mario, ventana, colores)
