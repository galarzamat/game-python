from principal import *
from configuracion import *
import random
import tkinter as tk
def ventana_notas(notificacion):
    msg = ""
    ventana_notas = tk.Tk()
    ventana_notas.title("")
    ventana_notas.config(width=700, height=100,bg='black')
    if notificacion == "largo":
        msg = "La palabra ingresada no es del mismo largo"
    if notificacion == "lemario":
        msg = "La palabra ingresada no esta en el lemario"

    mensaje_nota = tk.Label(text=msg)
    mensaje_nota.config(fg='white',bg='black',font=("assets/font.ttf", 23))
    mensaje_nota.place(x=50, y=20)
    ventana_notas.mainloop()


def enlista(valor, lista):
    for element in lista:
        if valor == element:
            return True
    return False

def quitar_salto(palabra):
    cadena = ""
    for letra in palabra:
        if letra == "\n":
            return cadena
        cadena = cadena + letra
    return cadena
def puntaje(correctas, casi, palabra):
    puntos = 0
    for letra in palabra:
        if enlista(letra, correctas):
            puntos += 10
        if enlista(letra, casi):
            puntos += 5
    return puntos


def palabraranmod(lista):
    palabra = random.choice(lista)
    return palabra


def lectura(archivo, salida, largo):
    lineas = archivo.readlines()
    for linea in lineas:
        cadena = quitar_salto(linea)
        if len(cadena) == largo:
            salida.append(cadena)
    print(salida)


def revision( palabracorrecta, palabra, correctas, incorrectas, casi):
    if palabracorrecta == palabra:
        return True
    else:
        for i in range(len(palabracorrecta)):
            if palabracorrecta[i] == palabra[i]:
                correctas.append(palabra[i])
            elif palabra[i] in palabracorrecta:
                casi.append(palabra[i])
            else:
                incorrectas.append(palabra[i])
        return False
