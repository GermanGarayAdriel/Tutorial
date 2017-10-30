from clases.Base import *

import pygame

ancho = 1280
alto = 720

class Mario(Base):

    def __init__(self):

        Base.__init__(self, 20, 600, 100, 100, "imagenes/mario/mario.png")

        self.estado = 0
        self.direccion = True
        self.detenido = False
        self.movimientos = ("imagenes/mario/mario.png", "imagenes/mario/mario_correr.png",
                            "imagenes/mario/mario_turbio.png", "imagenes/mario/mario_movimiento.png",
                            "imagenes/mario/mario_salto.png", "imagenes/invisiblex.png",
                            "imagenes/mario/mario_muerto.png",
                            "imagenes/mario/mario_bandera.png",)
        self.frame = 0
        self.maximo = 0
        self.salto = False
        self.bajando = False
        self.detenido = True

        self.terminado = False

        self.permitir_derecha = False
        self.permitir_izquierda = False
        self.permitir_salto = False

        Base.sprites_principales.add(self)

    def mover_derecha(self, velocidad, frames_totales):

        self.detenido = False

        if self.salto is False and self.bajando is False:
            if frames_totales - self.frame > 4:
                if self.estado <= 2:
                    self.estado += 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

                elif self.estado == 3:
                    self.estado = 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

        if self.permitir_derecha:
            self.rect.x += velocidad

    def mover_izquierda(self, velocidad, frames_totales):

        self.detenido = False

        if self.salto is False and self.bajando is False:
            if (frames_totales - self.frame) > 4:

                if self.estado == 0 or self.estado == 1 or self.estado == 2:
                    self.estado += 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

                elif self.estado == 3:
                    self.estado = 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

        if self.rect.x > -10:
            self.rect.x -= velocidad

    def cambiar_sprite(self, estado):
        self.image = pygame.image.load(self.movimientos[estado])
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.direccion is False:
            self.invertir()

    def invertir(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

