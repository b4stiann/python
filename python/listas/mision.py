#Bastian Rubilar

tareas = ['🏦 sacar dinero del banco ,'
          ' Hacer la colada' '🌳 Dar un paseo'
          '💈Cortarse el cabello' ,
          '🍵 Preparar el te'
          '📋Terminar el capitulo de listas' ,
          '📱Llamar a mama' , 
          '📺Ver My heroe Academia']

#Acceder a la primera tarea de la lista
print(tareas[0])

#Encontrar la segunda tarea de la lista
print(tareas[1])

#Obtener un subconjunto de tareas usando slicing (rebanado)
print(tareas[2:5])

#Intentar acceder a un indice inaxistente y manejar el error
try:
    print(tareas[10])
except:
    print('El error no existe')

#Modificar la lista para añadir una nueva tarea secreta sin usar .append()
tareas = tareas + ['📚Leer un libro']
print(tareas)