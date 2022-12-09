#! /usr/bin/env python
import os
import random
import sys
import pygame
import main
import funcionesVACIAS
from pygame.locals import *
from configuracion import *
from extras import *

# Funcion principal
def main(largo_elegido):
    if largo_elegido == "Facil":
        largo = LARGO_FACIL
    elif largo_elegido == "Medio":
        largo = LARGO_MEDIO
    elif largo_elegido == "Dificil":
        largo = LARGO_DIFICIL
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    palabrauser = ""
    listalemario = []
    palabrasuser = []
    correctas = []
    incorrectas = []
    casi = []
    gano = False
    archivo = open("data/lemario.txt", "r", encoding='utf-8-sig')
    # lectura del diccionario
    lectura(archivo, listalemario, largo)
    # elige una al azar
    palabraCorrecta = palabraranmod(listalemario)
    intentos = 5
    dibujar(screen, palabrasuser, palabrauser, puntos, segundos, gano, correctas, incorrectas, casi, largo,
            intentos)
    while segundos > fps / 1000 and intentos > 0 and not gano:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()
        if True:
            fps = 3
        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                archivo.close()
                pygame.quit()
                sys.exit()
            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                palabrauser += letra  # es la palabra que escribe el usuario
                if e.key == K_BACKSPACE:
                    palabrauser = palabrauser[0:len(palabrauser) - 1]
                if e.key == K_RETURN:
                    if len(palabrauser) == len(palabraCorrecta):
                        if enlista(palabrauser, listalemario):
                            gano = revision(palabraCorrecta, palabrauser, correctas, incorrectas, casi)
                            palabrasuser.append(palabrauser)
                            puntos += puntaje(correctas, casi, palabrauser)
                            palabrauser = ""
                            intentos -= 1
                        else:
                            ventana_notas("lemario")
                    else:
                        ventana_notas("largo")


        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, palabrasuser, palabrauser, puntos, segundos, gano, correctas, incorrectas, casi,
                largo, intentos)
        pygame.display.flip()
    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                archivo.close()
                pygame.quit()
                sys.exit()


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
