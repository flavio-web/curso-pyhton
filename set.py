#set o conjuntos. Son parecidos a los diccionarios pero no tienen clave valor y no se pueden repetir sus datos

frutas = {'Banana', 'Pera', 'Manzana', 'Banana', 'Pera'}
print( frutas ) #retorna => {'Banana', 'Pera', 'Manzana'}

#si quiero crear un conjutno vacio, debe de generarlo mediante set() no {} (Porque sino python entiende que quiero crear un diccionario)

#crea un conjunto vacio
letras = set()
print(letras)

#agregar un elemento
letras.add('A')
letras.add('B')
letras.add('C')
print(letras)

numeros = {1, 2 ,3}

#unir conjuntos
union = letras.union(numeros)
print(union)

#interseccion de conjuntos
intersec = letras.intersection(numeros)
print(intersec)
if( len(intersec) == 0 ):
    print("No existen datos iguales en los conjuntos")
