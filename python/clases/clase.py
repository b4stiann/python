class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def atributos(self):
        print(self.nombre, ";", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida> 0

    def morir (self):
        self.vida = 0
        print(self.nombre, "Ha Muerto")
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño (enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre,"ha realizado", daño, "puntos de daños a", enemigo.nombre )
        print("La vida de", enemigo.nombre, "es", enemigo.vida)
        if enemigo.esta_vivo():
            print("la vida de" , enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def get_fuerza(self):
        if fuerza < 0:
            print("La fuerza no puede ser negativa")
        else:
            self.fuerza = fuerza


class Guerrero(Personaje):
    def __init__(self, nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Selecciona un arma : (1) Acero Valyrio, daño 8. (2) MataDragones, daño 10"))
        if opcion == 1:
           self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Ingresa una opcion valida")
        
    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)

    def daño (self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre,fuerza,inteligencia,defensa,vida,libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro", self.libro)
    
    def daño (self, enemigo):
        return self.inteligencia* self.libro - enemigo.defensa


kaldrogo = Guerrero("Kaldrogo", 20, 30, 20, 100, 5)
mi_personaje = Personaje("Bastian", 20, 20, 10, 5)
gandalf = Mago("Alonso", 20, 30, 20, 100, 5)

mi_personaje.atacar(kaldrogo)
kaldrogo.atacar(gandalf)
gandalf.atacar(mi_personaje)

kaldrogo.atributos()
print("----------------")
mi_personaje.atributos()
print("----------------")
gandalf.atributos()

