


class Personaje:

    __personajes = []
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.__personajes.append({ "nombre": self.nombre, "fuerza": self.fuerza, "velocidad": self.velocidad })

    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    def __add__(self, otro_personaje):
        nuevo_nombre = self.nombre +'-'+otro_personaje.nombre
        nueva_fuerza = min((((self.fuerza + otro_personaje.fuerza) / 2) * 1.2), 100)
        nueva_velocidad =  min((((self.velocidad + otro_personaje.velocidad) / 2) * 1.2), 100)

        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

    @property
    def personajes(self):
        return self.__personajes
    
    
    
goku = Personaje('Goku', 80, 60)
vegeta = Personaje('Vegeta', 50, 75)

gogeta = goku + vegeta
print(gogeta)
print(gogeta.personajes)