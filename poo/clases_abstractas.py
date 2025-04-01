
#Las clases abstratcas son una plantilla de las cuales mediante la herencia, heredan todos los metodos y propiedades de la clase abstracta y no puede instanciarse

#Se debe primero importar ABC, abstractmethod
from abc import ABC, abstractmethod  


class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
    
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando: {self.actividad}")
        
        
            
atom = Estudiante("Atom", 7, "perro", "programación")
atom.presentarse()
atom.hacer_actividad()

felipe = Trabajador("Felipe", 35, "hombre", "jardinero")
felipe.presentarse()
felipe.hacer_actividad()
        