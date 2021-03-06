import pygame
from clases.Mario import Mario
from clases.Moneda import Moneda
from clases.Base import Base
from clases.Bloque import Bloque

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()
        #pygame.mouse.set_visible(False)

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):

        display = pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, colores):
        ventana.fill(colores['Blanco'])

    @classmethod
    def buscar_eventos(cls, mario):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cls.terminar()
                if evento.key == pygame.K_q:

                    if mario.direccion:
                        mario.permitir_derecha = True
                    if mario.direccion is False:
                        mario.permitir_izquierda = True

                if evento.key == pygame.K_e:
                    if mario.salto is False:
                        mario.permitir_derecha = False
                        mario.permitir_izquierda = False

                if evento.key == pygame.K_w:
                    mario.permitir_salto = True
                if evento.key == pygame.K_p:

                    mario.detenerse()

                    if mario.detenido:

                        mario.permitir_derecha = False
                        mario.permitir_izquierda = False

                        if mario.direccion:
                            mario.direccion = False
                        else:
                            mario.direccion = True

            if evento.type == pygame.KEYUP:
                if mario.bajando is False:
                    mario.detenerse()

    @classmethod
    def salto_mario(cls, mario, frames_totales):

        if mario.salto:
            mario.saltar(frames_totales)

    @classmethod
    def colisiones(cls, mario):

        control = False

        moneda = mario.colision(Base.monedas)
        if moneda is not False:
            moneda.agarrada()
            if moneda.identificador == 1:
                m = Moneda(120,290,2)
                bloque = Bloque(100,400)
            if moneda.identificador == 2:
                m = Moneda(350,600,3)
            if moneda.identificador == 3:
                for item in Base.bloques:
                    Base.bloques.remove(item)
                    Base.sprites.remove(item)
                mario.permitir = False

        # Mientras anda a pie
        if mario.salto is False:
            if mario.colision_piso() is False:
                if Controlador.colision_bloques(mario) is False:
                    control = True
                    mario.detenido = False
                    mario.caerse()

                if control is False:
                    if mario.bajando:
                        mario.detenerse()
                        mario.bajando = False

            elif mario.colision_piso():
                if mario.bajando:
                    mario.detenerse()
                    mario.bajando = False

    @classmethod
    def colision_bloques(cls, mario):
        bloque = mario.colision(Base.bloques)

        if bloque is not False:
            if mario.colision_bloques(bloque) is False:
                return True
        return False

    @classmethod
    def pausa(cls, mario, ventana):

        control = False

        pygame.draw.rect(ventana, (65, 105, 225), (375, 260, 500, 150), 10)
        Base.letras.draw(ventana)
        pygame.display.flip()

        while control is False:

            Controlador.buscar_eventos(mario)

            teclas = Controlador.buscar_teclas()

            if teclas[pygame.K_F2]:
                control = True

    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()