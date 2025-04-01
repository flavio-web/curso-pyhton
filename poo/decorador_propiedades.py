

class Persona:
    def __init__(self, nombre, edad = 1):
        self.__nombre = nombre
        self._edad = edad

    #El decorador property le permite acceder como si fuera a una propiedad en vez de un metodo
    @property
    def nombre(self):
        return self.__nombre
        
    
    #este decorador nos permite darle el valor como si fuera una propiedad en vez de un metodo. Y python puede destinguir cual es para getter y cual es para setter, incluso segun sus parametros, usando sobrecarga.

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
  
    #decorador que nos riev para eliminar una propiedad
    @nombre.deleter
    def nombre(self):
        #elimina una propiedad
        #del self.__nombre
        
        #para no eliminarla mejor le vamos a dar un nuevo valor
        self.__nombre = "Nombre eliminado!!!"
        


dalto = Persona("Dalto", 15)

#es por eso que podemos acceder a get_nombre como una propiedad sin los parentisis al final
nombre = dalto.nombre
print(nombre)

dalto.nombre = "Atom"
nombre = dalto.nombre
print(nombre)

del dalto.nombre
nombre = dalto.nombre
print(nombre)
        