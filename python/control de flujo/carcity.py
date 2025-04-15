#Bastian Rubilar
#03-04-2025

altura = int(input('¿Cual es tu altura? (cm) :'))

#Se creo una variable para solicitar la informacion del usuario
creditos = int(input('¿Cuantos creditos tienes? :'))

if altura >  137 and creditos >  10:
    print('Disfruta el viaje')
elif altura >  137 and creditos < 10:
    print('No puedes entrar')
elif creditos < 10 and altura >  137:
    print('No tienes suficientes creditos')
else:
    print('No tienes la altura ni los creditos suficientes para entrar')

