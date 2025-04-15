import random

# Lista de posibles respuestas
respuestas = [
    "Shi",
    "ño",
    "noshe",
    "puchapo",
    "no creo bro",
    "puede ser",
    "mejor te digo en otro momento",
    "mas tarde pregunta y quiza te diga",
    "no soy adivino asi q nose"
    "tralalero tralala "
    "uy , puede ser"
]

pregunta = input("Pregunta: ")

respuesta = random.choice(respuestas)

print(f"Respuesta: {respuesta}")
