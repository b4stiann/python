#Bastian Rubilar
#16-04-2025

def sumar(a, b, mostrar=False):
    resultado = a + b
    if mostrar:
        print(resultado)
    return resultado
def restar(a, b, mostrar=False):
    resultado = a - b
    if mostrar:
        print(resultado)
    return resultado
def multiplicar(a, b, mostrar=False):
    resultado = a * b
    if mostrar:
        print(resultado)
    return resultado
def dividir(a, b, mostrar=False):
    if b == 0:
        print("Error: División por cero")
        return None
    resultado = a / b
    if mostrar:
        print(resultado)
    return resultado
def potencia(a, b, mostrar=False):
    resultado = a ** b
    if mostrar:
        print(resultado)
    return resultado

sumar(5, 3, mostrar=True)
restar(5, 3, mostrar=True)
multiplicar(5, 3, mostrar=True)
dividir(5, 3, mostrar=True) 
potencia(5, 3, mostrar=True)