

class Automovil:
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self.estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Automovil()
mi_auto.conducir()