import math

#Funciones manejo de cadenas (str) y numeros

nombre = "Atomcito"
edad = "8"

#longuitud de la variable
print("El nombre",nombre, "tiene",len(nombre), "caracteres")

#encontrar caracteres en variable
caracter = "t"
print("el caracter",caracter,"esta en la posicion:", nombre.find(caracter))

#valida si el contendio de la variable son digitos/numeros pero en cadena de texto
print( edad.isdigit() )

#capitalizar letras
print( nombre.capitalize() )

#convertir a mayusculas
print( nombre.upper() )

#convertir a minusculas
print( nombre.lower() )

#cuentas veces se repite una letra
print( nombre.count("o") )

#validar si solo tiene letras
print( nombre.isalpha() )

#Funciones de numeros

pi = 3.1416

#redondear a 2 decimales o al numero de decimales que le coloquemos
print( round(pi,2) )

#redondear hacia arriba
print( round(pi) )  

#redondear hacia abajo
print( int(pi) )    #int() convierte a entero

#convertir a flotante
print( float(edad) )    #float() convierte a flotante   #float() convierte a flotante


#raiz cuadrada
print( math.sqrt(pi) )

#potencia
print( math.pow(2,3) )

#retorna el valor absoluto
print( abs(pi) )

#redondear hacia arriba
print( math.ceil(pi) )

#redondear hacia abajo
print( math.floor(pi) )

#valor minimo y maximo entre una serie de numeros
a = 5
b = 3
c = 8

print( max( a, b, c) )
print( min( a, b, c) )