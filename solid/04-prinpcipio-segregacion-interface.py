#PRINICIPIO DE SEGREGACION DE LA INTERFACE
#Este prinpcio nos dice que a un cliente (clase) no este obligada a usar interfaces (metodos) que no son necesarios para su creacion

#Entonces creamos varias clases abstractas para que al heredarlas no esten atadas a implementar todos los metodos abstractos

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass
    
class Humano(Trabajador, Durmiente, Comedor):
    def trabajar(self):
        print("El humano esta trabajando...")
        
    def dormir(self):
        print("El humano esta durmiendo...")
        
    def comer(self):
        print("El humano esta comiendo...")
        
        
class Robot(Trabajador):
     def trabajar(self):
        print("El robot esta trabajando...")
        
        
humano = Humano()
humano.trabajar()
humano.comer()
humano.dormir()

robot = Robot()
robot.trabajar()