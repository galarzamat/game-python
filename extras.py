import sys

import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
import tkinter as tk


def cerrar_juego():
    pygame.quit()
    sys.exit()


def ventana_secundaria(puntos):
    ventana_secundaria = tk.Tk()
    ventana_secundaria.title("Menu")
    ventana_secundaria.config(width=400, height=200, bg='black')

    mensaje_ganaste = tk.Label(text="Felicidades Ganaste")
    mensaje_ganaste.config(fg='white', bg='black', font=("assets/font.ttf", 23))
    mensaje_ganaste.place(x=50, y=20)
    mensaje_puntos = tk.Label(text="Puntos totales: " + str(puntos))
    mensaje_puntos.config(fg='white', bg='black', font=("assets/font.ttf", 23))
    mensaje_puntos.place(x=50, y=50)

    cerrar = tk.Button(text="Cerrar Juego", command=cerrar_juego, compound=tk.CENTER)
    cerrar.config(font=23, borderwidth=0)
    cerrar.place(x=150, y=100)

    ventana_secundaria.mainloop()


def dameLetraApretada(key):
    if key == K_a:
        return ("a")
    elif key == K_b:
        return ("b")
    elif key == K_c:
        return ("c")
    elif key == K_d:
        return ("d")
    elif key == K_e:
        return ("e")
    elif key == K_f:
        return ("f")
    elif key == K_g:
        return ("g")
    elif key == K_h:
        return ("h")
    elif key == K_i:
        return ("i")
    elif key == K_j:
        return ("j")
    elif key == K_k:
        return ("k")
    elif key == K_l:
        return ("l")
    elif key == K_m:
        return ("m")
    elif key == K_n:
        return ("n")
    elif key == 241:
        return ("ñ")
    elif key == K_o:
        return ("o")
    elif key == K_p:
        return ("p")
    elif key == K_q:
        return ("q")
    elif key == K_r:
        return ("r")
    elif key == K_s:
        return ("s")
    elif key == K_t:
        return ("t")
    elif key == K_u:
        return ("u")
    elif key == K_v:
        return ("v")
    elif key == K_w:
        return ("w")
    elif key == K_x:
        return ("x")
    elif key == K_y:
        return ("y")
    elif key == K_z:
        return ("z")
    elif key == K_SLASH:
        return ("-")
    elif key == K_KP_MINUS:
        return ("-")
    elif key == K_SPACE:
        return (" ")
    else:
        return ("")


def show_text(screen, font, texto, color, x, y):
    tipo_font = pygame.font.Font(font, 20)
    text = tipo_font.render(texto, True, color)
    rectangulo = text.get_rect()
    rectangulo.center = (x, y)
    screen.blit(text, rectangulo)


def mensaje(gano, intentos, puntos):
    if gano:
        ventana_secundaria(puntos)
    elif intentos == 0:
        return "Se acabaron los intentos :("
    elif intentos == 5:
        return "Adivine la palabra "
    else:
        return "Fallaste :("


def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, largo,
            intentos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    #El mensaje le ayuda al usuario si fallo o no el intento
    show_text(screen, 'assets/font.ttf', mensaje(gano, intentos, puntos), COLOR_TEXTO, screen.get_rect().centerx, 515)
    # Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)
    # muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_BLANCO), (190, 570))
    # muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    # muestra los segundos y puede cambiar de color con el tiempo
    if (segundos < 15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))
    show_text(screen, 'assets/font.ttf', "intentos:" + str(intentos), COLOR_BLANCO, screen.get_rect().centerx, 20)
    # muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_BLANCO),
                    (ANCHO // 2 - len(palabra) * TAMANNO_LETRA_GRANDE // 4, 20 + 80 * pos))
        pos += 1

    abcdario = ["q  w  e  r  t  y  u  i  o  p", "a  s  d  f  g  h  j  k  l  m", "z  x  c  v  b  n  ñ"]
    y = 30
    for abc in abcdario:
        x = 0.4
        for letra in abc:
            if letra in correctas:
                show_text(screen, 'assets/font.ttf', letra, COLOR_LETRAS, 150 + x, ALTO / 1.5 + y)
            elif letra in incorrectas:
                show_text(screen, 'assets/font.ttf', letra, COLOR_ROJO, 150 + x, ALTO / 1.5 + y)
            elif letra in casi:
                show_text(screen, 'assets/font.ttf', letra, COLOR_AMARILLO, 150 + x, ALTO / 1.5 + y)
            else:
                show_text(screen, 'assets/font.ttf', letra, COLOR_BLANCO, 150 + x, ALTO / 1.5 + y)
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA
