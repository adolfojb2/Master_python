from persona import Persona
from zombi import Zombi
import os

os.system("cls")

print()
print("La ciudad se ha llenado de zombis.")
print("Estás en la calle 1 y has de llegar")
print("a la calle 40 para poder salvarte.")
print()
print("Los zombis avanzan 1, 2 ó 3 calles.")
print("Tú puedes avanzar 1, 2 ó 3 calles.")
print()
nombre = input("  ¿Estás preparado? ¿Cuál es tu nombre?: ").capitalize()

jugador = Persona(nombre)

horda = [] #Lista de objetos tipo zombi
for i in range(10):
    z = Zombi()
    horda.append(z)

while True:
    os.system("cls")
    print(jugador.estado())

    calles = [] #calles actuales donde se encuentran los zombis
    for zombi in horda:
        if not zombi.no_visible():
            calles.append(zombi.calle)
    calles.sort()
    print("Hay zombis en las calles: ")
    for elemento in calles:
        print(elemento, end=" ")
    print()

    if jugador.calle >= 40:
        print("Has llegado a la calle 40, GANASTE!!!")
        print()
        break
    
    comido = False
    for zombi in horda:
        if zombi.calle == jugador.calle:
            comido = True
    if comido:
        print("Un zombi te acaba de ver.")
        print("Te va ha commer, se acabó el juego.")
        print()
        break

    velocidad = 0
    while velocidad not in (1,2,3):
        velocidad = int(input("Cuanto quieres correr (1/2/3): "))
    jugador.moverse(velocidad)

    for z in horda:
        z.moverse()
        if z.no_visible():
            horda.remove(z)