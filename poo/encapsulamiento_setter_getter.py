

class Persona:
    def __init__(self, nombre, edad = 1):
        self.__nombre = nombre
        self.__edad = edad

    #de esta manera accedemos a los datos privados (encapsulados) en la clase
    def get_nombre(self):
        return self.__nombre
    
    #de esta manera le damos un valor a una propiedad muy privada (encapsulada)
    def set_nombre(self, nombre):
        self.__nombre = nombre


dalto = Persona("Dalto", 15)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Atom")
nombre = dalto.get_nombre()
print(nombre)

        