from archivos.dibujo import *
from archivos.procesos import *
from clases.Piso import *
from clases.Bloque import Bloque
from clases.Moneda import Moneda

def nivel(reloj, mario, ventana, colores):

    FPS = 120

    frames_totales = 0

    #pygame.mixer.music.load("musica/juego.wav")
    #pygame.mixer.music.play(10,0)
    #pygame.mixer.music.set_volume(0.5)

    x = 0

    for i in range(40):
        piso = Piso(x,695)
        x += 72

    bloque = Bloque(400,400)
    moneda = Moneda(500,600)

    while True:

        procesos(reloj, mario, FPS, frames_totales)

        dibujo(ventana, colores)

        frames_totales += 1
        print(mario.rect.x)