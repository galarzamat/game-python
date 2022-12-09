import pygame, sys
from button import Button
from configuracion import *
import principal

pygame.init()

screen = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("black")

        DIFICULTAD_FACIL = Button(image=None, pos=(430, 150),
                                  text_input="Facil - (4 letras)", font=get_font(30), base_color="white",
                                  hovering_color="#dac9c9")
        DIFICULTAD_MEDIO = Button(image=None, pos=(430, 250),
                                  text_input="Medio - (6 letras)", font=get_font(30), base_color="white",
                                  hovering_color="#dac9c9")
        DIFICULTAD_DIFICIL = Button(image=None, pos=(430, 350),
                                    text_input="Dificil - (8 letras)", font=get_font(30), base_color="white",
                                    hovering_color="#dac9c9")

        for button in [DIFICULTAD_FACIL, DIFICULTAD_MEDIO, DIFICULTAD_DIFICIL]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        PLAY_BACK = Button(image=None, pos=(430, 550),
                           text_input="Atras", font=get_font(50), base_color="White", hovering_color="#dac9c9")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DIFICULTAD_FACIL.checkForInput(PLAY_MOUSE_POS):
                    principal.main("Facil")
                if DIFICULTAD_MEDIO.checkForInput(PLAY_MOUSE_POS):
                    principal.main("Medio")
                if DIFICULTAD_DIFICIL.checkForInput(PLAY_MOUSE_POS):
                    principal.main("Dificil")
        pygame.display.update()


def ayuda():
    pass


def main_menu():
    while True:
        screen.blit(fondo, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MENU PRINCIPAL", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(430, 100))

        PLAY_BUTTON = Button(image=None, pos=(450, 220),
                             text_input="Jugar", font=get_font(50), base_color="white",
                             hovering_color="#dac9c9")

        QUIT_BUTTON = Button(image=None, pos=(450, 500),
                             text_input="Quitar", font=get_font(50), base_color="white",
                             hovering_color="#dac9c9")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


main_menu()
