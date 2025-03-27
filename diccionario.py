#se los realiza mediante llaves, las claves deben ser unicas, tipo json

persona = {
    'nombre': 'Atom',
    'edad': 8,
    'telefono': '1234656',
    'isAdmin': True,
    'eats': ['Pollo', 'Atun', 'Fideos', 'Pescado']
}

print( persona )

#acceder a la clave nombre
print( persona['nombre'] )

#agregar una nueva clave - valor
persona['email'] = 'atom@gmail.com'
print( persona )

#agregar una nueva comida favorita a la lista eats del diccionario persona
persona['eats'].append('Camarones')
print( persona )

#esta es otra forma de acceder al valor de una clave
edad = persona.get("edad")
print("Edad es: ", edad)

#muestra las claves del diccionario
print( persona.keys() )

#muestra los valores
print( persona.values() )

#muestra los valores
print( persona.items() )

#elimina una clave
print( persona.pop('telefono') )
print( persona )

#accede a un elemento y no enceuntra la clave devuelve el valor por default
print( persona.get('direccion', 'Machala'))


#actualiza elemento o lo agrega en caso de no existir
print( persona.update({'direccion': 'Machala'}) )
print( persona )

#eliminar todo el diccionario
print( persona.clear() )