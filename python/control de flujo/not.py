#Bastian Rubilar
#02-04-2025

respuesta = input('¿estas cansado? ( si / no) : ').strip().lower()

cansado = respuesta == 'si'

if not cansado:
    print('!Es hora de programar!')
else:
    print('Tomate un descanso , lo necesitas')
