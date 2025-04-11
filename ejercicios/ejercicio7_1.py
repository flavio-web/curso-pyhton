


class Personaje:

    __personajes = []
        
    def newPersonaje(self, nombre, fuerza, velocidad):
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
    
    def existePersonaje(self, nombrePersonaje):
        for personaje in self.__personajes:
            if personaje.nombre.lower() == nombrePersonaje.lower():
                return True
            
        return False

    @property
    def personajes(self):
        return self.__personajes
    
    
    
print("*** Menu de opciones ***\n 1.Registrar personaje\n 2.Fusionar personajes\n 3.listar Personajes")

while True:
    option = int(input('Ingrese una opcion del menu: '))
    if( option >= 1 | option <= 3):
        break        
    print("Error. La opcion selecionada es incorrecta")   
    
print("genial saliste del bucle")

personaje = Personaje()

if option == 1:
    nombrePersonaje = ""
    while True:
        nombrePersonaje = input('Ingrese el nombre del personaje:')
        existe = personaje.existePersonaje( nombrePersonaje )
        if( existe == False ):
            break
        print(f"El personaje {nombrePersonaje} ya existe, ingrese otro nombre de personaje")
        
    fuerzaPersonaje = float(input("Ingrese el valor del fuerza del personaje entre 0 - 100:"))
    velocidadPersonaje = float(input("Ingrese el valor de velocidad del personaje entre 0 - 100:"))
    
    personaje.newPersonaje(nombrePersonaje, velocidadPersonaje, fuerzaPersonaje)
    print(f"Personaje {nombrePersonaje} registrado correctamente")
    print(personaje.personajes)
    
    
# goku = Personaje('Goku', 80, 60)
# vegeta = Personaje('Vegeta', 50, 75)

# gogeta = goku + vegeta
# print(gogeta)
# print(gogeta.personajes)