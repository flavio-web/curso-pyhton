#Las funcjones especiales sonmpropios de python y empiezan con dos guiones bajo y terminan con dos guiones bajo como __init__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       
    #deveulve el objeto en representacion de texto 
    def __str__(self):
        return f'Persona(nombre={self.nombre}), edad={self.edad}'
    
    
    def __repr__(self):
        return f'Persona("{self.nombre}", edad={self.edad})'
    
    #sobrecarga de operadores
    #sirve para sumar objetos (clases) y que pasa con sus propiedades. En este caso se concatenan los nombre y se suman las edades
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    
    
atom = Persona("Atom", 7)
print(atom)

#Deveuelve el objeto como representacion de texto
repre = repr(atom)
print(repre)

#eval() convierte el texto a objeto
resultado = eval(repre)
print(resultado.nombre)

pedro = Persona("Pedro", 10)
nuevaPersona = atom + pedro
print(nuevaPersona)
print(nuevaPersona.nombre)
print(nuevaPersona.edad)