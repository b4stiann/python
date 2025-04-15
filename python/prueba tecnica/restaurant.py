#Bastian Rubilar
#08-04-2025

valoracion = float(input('Ingresa la valoracion del restaurante (1-5) :'))

if valoracion > 4.5 :
    print('El restaurante es extraordinario')
elif valoracion > 4:
    print('El restaurante es excelente')
elif valoracion > 3 :
    print('El restaurante es bueno')
elif valoracion > 2 :
    print('El restaurante es regular')
elif valoracion > 1 :
    print('El restaurante es pesimo')
else:
    print('Pesimo')
