#Bastian Rubilar
#07-03-2025
#

print('Banco del 4°B)')

pin = int(input('Ingresa tu pin : '))

while pin !=1234:
    pin = int (input('PIN incorrecto. Ingresa tu PIN nuevamente'))

if pin ==1234:
    print('PIN aceptado!')
    print('Bienvenido a tu cuenta')