#Bastian Rubilar
#30-04-2025

import random

print("¡Adivina la suma de los dados!")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
total = dado1 + dado2

intentos = 0
while True:
    intentos += 1
    adivinanza = int(input("¿Cual es el total ( entre 2 y 12)?"))
    if adivinanza == total:
        print(f" ¡Lo adivinaste en {intentos} intento(s)! El total era {total}.")
        break
    else:
        print("Intenta de nuevo...") 