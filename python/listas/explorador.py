#Bastian Rubilar
#
#17-03-2025

Verdura = ('lechuga', 'pepino', 'cebolla', 'tomate' , 'zanahoria')

verdura_lista = list(Verdura)

verdura_lista[-1] = 'zanahoria'

verdura_lista.append('zanahoria')

Verdura = tuple(verdura_lista)

print(Verdura)  