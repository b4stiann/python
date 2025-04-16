#Bastian Rubilar
#14-04-2025

import random

def fortuna():
    numero = random.randint(1,8)
    if numero == 1:
        print("no persigas la felicidad, creala")
    elif numero == 2:
        print("Todas las cosas son dificiles antes de ser faciles")
    elif numero == 3:
        print("El pajaro madrugador consigue el gusano, pero el segundo raton se lleva el queso")
    elif numero == 4:
        print("Alguien en tu vida necesita una carta de tu parte")
    elif numero == 5:
        print("No solo pienses. ¡Actua!")
    elif numero == 6:
        print("Tu corazon se acelerara")
    elif numero == 7:
        print("La fortuna que buscas esta en otra galleta")
    else:
        print("¡Ayuda! ¡Estoy prisionero en una panaderia china!")
    
fortuna()