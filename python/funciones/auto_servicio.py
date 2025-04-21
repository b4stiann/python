#Bastian Rubilar
#21-04-2025

def obtener_articulo(numero):
    if numero == 1 :
        return "Hamburguesa con queso"
    elif numero == 2 :
        return "Papas fritas"
    elif numero == 3 :
        return "Refresco"
    elif numero == 4 :
        return "Helado"
    elif numero == 5 :
        return "Galleta"
    else :
        return "Articulo no disponible"

def Bienvenida():
    print("¡Bienvenida al Auto-Servicio de Comida Rapida!")
    print("Menu :")
    print("1.Hamburguesa con queso")
    print("2.Papas Fritas")
    print("3.Refresco")
    print("4.Helado")
    print("5.Galleta")

Bienvenida()
numero = int(input("Por Favor, introduce el numero del articulo que deseas pedir :"))
print("Has pedido:", obtener_articulo(numero))
print("Gracias por tu pedido, ¡disfruta tu comida!")