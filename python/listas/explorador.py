#Bastian Rubilar
#Bueno para jugar futbol
#17-03-2025

Verdura = ('lechuga', 'pepino', 'cebolla', 'tomate' , 'zanahoria')

verdura_lista = list(Verdura)

#Cambiar ultimo valor de la lista

verdura_lista[-1] = 'zanahoria'

#Agregar nuevo valor al final de la lista

verdura_lista.append('zanahoria')

#Insertar un elemento en la segunda posicion  de la lista con .insert()

verdura_lista.insert(2, 'papa')

#Eliminia un elemento de la lista con .remove()

verdura_lista.remove('pepino')

#Encuentra la posicion de un elemento especifico con .index()

posicion = verdura_lista.index('tomate')

#Ordenar la lista en un orden alfabetico

verdura_lista.sort()

#Invertir el orden de la lista

verdura_lista.reverse()