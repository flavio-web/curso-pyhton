
#Es una especia de funcion callback de javascript
#Y no sirve para agregar codigo antes o despues de ejecutar la funcion que enviamos como argumento
def decorador( funcion ):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

#Esto e sla funciona antigua de llamarlo
""" def saludo():
    print("Hola Atom como estas")
    
saludo_modificado = decorador(saludo)
saludo_modificado() """


#Esta es la manera moderna utilizando los decoradores, que por casuludad mi @decorador se llama decorador() como el metodo

#llamamos a la funcion decorador con un arroba
@decorador
def saludo():
    print("Hola Atom como estas")
    
saludo()