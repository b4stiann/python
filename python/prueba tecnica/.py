#Bastian Rubilar
#08-04-2025

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("P1) ¿Te gusta mas el amanecer o el atardecer? : ")
print("1) Amanecer")
print("2) Atardecer")
respuesta1 = input("Ingresa 1 o 2 : ")

if respuesta1 == "1" :
    gryffindor += 1
    ravenclaw += 1
elif respuesta1 == "2" :
    hufflepuff += 1
    slytherin += 1
else:
    print("Entrada Incorrecta.")

print("\nP2) Cuando muera quiero que la gente me recuerde como :")
print("1) El bueno")
print("2)El grande")
print("3) El sabio")
print("4) El valiente")
respuesta3 = input("Ingresa 1, 2, 3 o 4 : ")

if respuesta3 == "1" :
    slytherin += 4
elif respuesta3 == "2" :
    hufflepuff += 4
elif respuesta3 == "3" :
    ravenclaw += 4
elif respuesta3 == "4" :
    gryffindor += 4
else:
    print("Entrada Incorrecta.")

print("\nPuntajes finales :")
print("Gryffindor :",  gryffindor)
print("Ravenclaw :" ,  ravenclaw)
print("Hufflepuff :", hufflepuff)
print("Slytherin :",  slytherin)

puntajes = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

casa_ganadora = max(puntajes, key=puntajes.get)
print("\nLa casa con mas puntos es :", casa_ganadora)