#Bastian Rubilar
#24-03-2025

#Ejercicio 1: Basico
print("Ejercicio 1: Basico")
for i in range(101):
    print(i)

#Ejercicio 2: Multiples de 2
print("\nEjercicio 2: Multiples de 2")
for i in range(2, 501, 2):
    print(i)

# Ejercicio 3: Contando Vanilla Ice
print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Ejercicio 4: Wow. Numero gigante a la vista

print("\nEjercicio4: Wow Numero gigante a la vista")
suma_pares = sum(i for i in range(0, 500001, 2))
print("La suma de los numeros pares del 0 al 500,00 es:", suma_pares)

#Ejercicio 5: Regresame al 3
print("\Ejercicio 5: Regresame al 3")
for i in range(2024, 0, -3):
    print(i)

#Ejercicio 6: Contador dinamico
print("\Ejercicio 6: Contador dinamico")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0 :
        print(i)