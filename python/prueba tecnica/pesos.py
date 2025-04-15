#Bastian Rubilar
#08-04-2025

peso_tierra = float(input('Cual es tu peso en la tierra? : '))

print("Elige un planeta :")
print('1. Mercurio')
print('2. Venus')
print('3. Marte')
print('4. Jupiter')
print('5. Saturno')
print('6. Urano')
print('7. Neptuno')

planeta = int(input('Ingresa el numero del planeta (1-7): '))

if planeta == 1:
    gravedad = 0.38
elif planeta == 2:
    gravedad = 0.91
elif planeta == 3:  
    gravedad = 0.38
elif planeta == 4:
    gravedad = 2.53
elif planeta == 5:
    gravedad = 1.07
elif planeta == 6:
    gravedad = 0.89
elif planeta == 7:
    gravedad = 1.14
else: 
    print('Numero de planeta no valido')
    exit()

peso_nuevo = peso_tierra * gravedad
print(f'Tu peso en el planeta seleccionado seria : {peso_nuevo :.2f}kg')
