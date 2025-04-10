#Principio de responsabilidad unica. Todas las clases y metodos deben de tener una unica responsabilidad, es por eso que en este ejemplo dividimos el tanque de combustible y el auto. Porque el auto tenemos las funciones de mover y en la clase tanque tenemos las funciones para recargar y obtener la cantidad de combustible
class TanqueCombustible():
    def __init__(self):
        self.combustible = 100
        
    def agregarCombustible(self, cantidad):
        self.combustible += cantidad
        
    def obtenerCombustible(self):
        return self.combustible
    
    def usarCombustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtenerCombustible() >= distancia / 2:
           self.posicion += distancia
           self.tanque.usarCombustible( distancia / 2 )
           print("Has movido el auto excitosamente")
        else:
           print("No hay suficiente combustible")
           
    def obtenerPosicion(self):
        return self.posicion
    
tanque = TanqueCombustible()
miAuto = Auto(tanque)

print("Posicion:", miAuto.obtenerPosicion() )
miAuto.mover(20)

print("Posicion:", miAuto.obtenerPosicion() )
miAuto.mover(40)

print("Posicion:", miAuto.obtenerPosicion() )
miAuto.mover(60)

print("Posicion:", miAuto.obtenerPosicion() )
miAuto.mover(80)

print("Posicion:", miAuto.obtenerPosicion() )
miAuto.mover(100)

print("Posicion:", miAuto.obtenerPosicion() )
