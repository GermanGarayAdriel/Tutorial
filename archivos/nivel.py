from archivos.dibujo import *
from archivos.procesos import *
from clases.Piso import *
from clases.Letras import Letra
from clases.Bloque import Bloque
from clases.Moneda import Moneda

def nivel(reloj, mario, ventana, colores):

    FPS = 120

    frames_totales = 0

    #pygame.mixer.music.load("musica/juego.wav")
    #pygame.mixer.music.play(10,0)
    #pygame.mixer.music.set_volume(0.5)

    m = Moneda(700,600,1)

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")

    x = 0

    for i in range(40):
        piso = Piso(x,695)
        x += 72


    while True:

        procesos(reloj, mario, FPS, frames_totales, ventana)

        dibujo(ventana, colores)

        frames_totales += 1