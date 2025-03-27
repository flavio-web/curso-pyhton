 
nombres = ['Liuis', 'Maria', 'Jose', 'Ana', 'Pedro', 'Luisa', 'Carlos', 'Sofia', 'Manuel', 'Laura']
nuevosNombres = [None] * len(nombres)  # Inicializamos la lista con elementos vacíos
for index, nombre in enumerate(nombres):
    print(nombre)
    nuevosNombres[index] = nombre

print(nuevosNombres)

#mostrar ultimo elemento de la lista
print( nombres[-1] )

#agregar un elemento al final de una lista
nombres.append('LILI')
print(nombres)

#inserta un elemento a la posicion en la que deseamos y corre el resto de elementos
nombres.insert(-1, 'Atom')
print(nombres)

#eliminar un elemento - este elemento es distinguible en mayus and minus, solo se puede usar remoive en strings
print("----- elimianr el elemento LILI -----")
nombres.remove('LILI')
print(nombres)

#elimina elemento de cualquier tipo, mediante el index
nombres.pop(1)
print(nombres)

#limpiar la lista
print("----- limpiar la lista -----")
nuevosNombres.clear()
print(nuevosNombres)