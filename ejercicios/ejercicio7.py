"""
El juego consiste en crear persionajes de un juego y que estos oersinahjes se puedan fusionar para formas personas mas poderosos

Para ello debemos cambiar el comportamient del operador '+' para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas

Una posible formula es; el promedio de las habilidades de ambos, al cuadrado!
"""

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'
    
    def __add__(self, otro_personaje):
        nuevo_nombre = self.nombre +'-'+otro_personaje.nombre
        nueva_fuerza = min((((self.fuerza + otro_personaje.fuerza) / 2) * 1.2), 100)
        nueva_velocidad =  min((((self.velocidad + otro_personaje.velocidad) / 2) * 1.2), 100)

        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    

goku = Personaje('Goku', 80, 60)
vegeta = Personaje('Vegeta', 50, 75)

gogeta = goku + vegeta

print(goku)
print(vegeta)
print(gogeta)