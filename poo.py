#Programacion orientada a objetos

class Persona:
   
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludar(self):
        print("Hola, yo me llamo ",self.nombre, self.apellido)

      
class Cliente( Persona ):
    def saludar(self):  
        print("Hola desde la clase cliente al usuario", self.nombre, self.apellido)
    
pablo = Persona("Pablo", "Lopez")
pepe = Persona("Pepe", "Roman")

pablo.saludar()
pepe.saludar()

ana = Cliente("Ana", 'Perez')
ana.saludar()
