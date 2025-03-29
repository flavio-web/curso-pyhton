"""
Simular la gestion de un biblioteca

Crear una aplicacion de consola simple para gestionar una biblioteca
Este permitira agregar libros,buscar libros por titulo y autor y mostrar todos los libros disponibles.

"""

class Libro:
    def __init__(self, titulo, autor, anio, isbn):
        self.titulo = titulo
        self.autor  = autor
        self.anio   = anio
        self.isbn   = isbn
        
    def __str__(self):
        return f'{self.titulo} por {self.autor} ({self.anio} - ${self.isbn})'

class Biblioteca(Libro):
    def __init__(self):
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def buscar_libro(self, search):
        return [ libro for libro in self.libros if search.lower() in libro.titulo.lower() or search.lower() in libro.autor.lower() ]
        #return list(filter( lambda libro: libro['titulo'].lower() == search.lower() or libro['autor'].lower() == search.lower(), self.libros ))
        
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)
            

libro1 = Libro("Sangre de campeon", "Carlos Cuauhtémoc Sánchez", "2001", "458945")
libro2 = Libro("Don Quijote", "Miguel De Servantes", "1604", "898481")
libro3 = Libro("El Alquimista", "Paulo Coelho", "1988", "897946165")
libro4 = Libro("El Alquimista 2", "Paulo Coelho", "1998", "8/89115110")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

#biblioteca.mostrar_libros()
search = input("Buscar Libro: ")
libros_encontrados = biblioteca.buscar_libro(search)
if( len(libros_encontrados) == 0 ):
    print("No existen coincidencias de libros con ", search)
for libro in libros_encontrados:
    print(libro)
