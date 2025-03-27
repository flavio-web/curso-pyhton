
#En las tuplas no se puede agregar, eliminar o modificar el elemento de una posicion, solo puedo acceder a los elementos y a su longuitud. Las tuplas no cambian ni se inmutan.

miTupa = ('Marcos', 'Maria', 'Jose', 'Maria')
print(miTupa)

#acceder a un elemento de una tupla
print(miTupa[1])

#muestra los elementos desde la posicion 1 hasta un elemento antes de la posicion 3
print(miTupa[1:3])

#muestra los elementos de dos en dos
print(miTupa[::2])

#muestra la longuitud de las tuplas
print(len(miTupa) ) 

#muestra el index del elemento
print( miTupa.index('Jose') )


#asignar valores a variables mediante una tupla
misDatos = ('Flavio', 31, 'flavio@gmail.com')
nombre, edad, email = misDatos

print(nombre)
print(edad)
print(email)