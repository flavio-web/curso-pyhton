class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")
        

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def show_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def show_habilidad(self):
        print(f"Sow {self.nombre} y mi habilidad es: {self.habilidad}")
        
    def presentarsePadre(self):
        #esto se utiliza en las herencias para acceder a los metodos de la clase padre
        super().show_habilidad()
    def presentarseDesdeClase(self):
        #de esta manera accedemos a los metodos de esta misma clase
        self.show_habilidad()
        

roberto = EmpleadoArtista("Roberto", 35, "argentino", "cantar", 1500, "SODINFO CIA LTDA")
roberto.presentarsePadre()
roberto.presentarseDesdeClase()

