#Bastian Rubilar
#15-05-2025

# Ejercicio 1: Cambia los valores de las siguientes variables y muestra el resultado en consola.
matriz = [ [10, 15, 20], [3, 7, 14] ]

futbolistas = [

   {"nombre": "Cristiano Ronaldo", "pais": "Portugal"},

   {"nombre": "Lionel Messi", "pais": "Argentina"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
print(matriz)

# Cambia el nombre del primer futbolista de “Cristiano Ronaldo” a “Lionel Messi”

futbolistas[0]["nombre"] = "Cristiano Ronaldo"
print(futbolistas)

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(ciudades)

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#Ejercicio 2: Iterar a través de una lista de diccionarios
#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.

futbolistas = [

   {"nombre": "Cristiano Ronaldo", "pais": "Portugal"},

   {"nombre": "Lionel Messi", "pais": "Argentina"},

   {"nombre": "Neymar Jr", "pais": "Brasil"},

   {"nombre": "Kylian Mbappe","pais": "Francia"}

]


def iterarDiccionario(listas):
    for diccionario in listas:
        print("," .join(f"{key} - {value}" for key, value in diccionario.items()))
iterarDiccionario(futbolistas)

#Ejercicio 3:Obtener valores de una lista de diccionarios
#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
#La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista.

def iterarDiccionario2(futbolistas, nac):
    for diccionario in nac:
        if futbolistas in diccionario:
            print(diccionario[futbolistas])

#Ejemplo de uso

iterarDiccionario2("nombre", futbolistas)
iterarDiccionario2("nac", futbolistas)

#Ejercicio 4:  Iterar a través de un diccionario con valores de lista
#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas.
#La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}
def informacionDiccionario(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

print("\n Iterar a traves de un diccionario con valores de la lista")

informacionDiccionario(costa_rica)