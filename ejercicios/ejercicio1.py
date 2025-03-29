#Crear una funcion que nos permita generar contraseñas aleatorias de una cantidad de caracteres ingresada por el teclado.

import random
import string

def passwordGenerator( cantidad = 10 ):
    #todas las letras en mayusculas
    str1 = string.ascii_uppercase 
    
    #todas las letras en minusculas
    str2 = string.ascii_lowercase
    
    #todos los numeros
    str3 = string.digits
    
    #todos los cacracteres especiales
    str4 = string.punctuation
    #print( str1, str2, str3, str4 )
    
    #creamos una lista vacia y le vamos agregando los string en forma de lista
    s = []
    s.extend( list(str1) )
    s.extend( list(str2) )
    s.extend( list(str3) )
    s.extend( list(str4) )
    
    #de forma aleatoria ordenamos la lista
    random.shuffle(s)
    #print(s)
    
    #retornamos la cantidad de elementos
    return ("".join(s[:cantidad]))

cantidad = int(input("Ingrese la cantidad de letras de la contraseña: "))

password = passwordGenerator( cantidad )
print("Contraseña generada", password)
