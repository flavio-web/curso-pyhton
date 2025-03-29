class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")
        

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.salario = salario
        
    
    
roberto = Empleado("Roberto", 35, "ecuatoriana", 1500)
roberto.hablar()