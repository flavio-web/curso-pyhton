#crear una funcion que nos permita convertir grados Celcius a Farihen y visceversa

def celsius_to_fahrenheit( celsius ):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius( fahrenheit ):
    return ( fahrenheit - 32 ) * 5/9

def conversor():
    print("Seleccionar una conversion")
    print("1. Celsius a Fahreheint")
    print("2. Fahreheint a Celsius")
    
    option = int(input("Ingrese la opcion: "))
    
    if( option < 1 or option > 2 ):
        print("Error al momento de seleccionar la opcion")
        conversor()
        return
    
    if( option == 1 ):
        celsius = float(input("Ingrese la temperatura en celcius:"))
        resultado = celsius_to_fahrenheit( celsius )
    else:
        fahrenheit = float(input("Ingrese la temperatura en celcius:"))
        resultado = fahrenheit_to_celsius( fahrenheit )
        
    print("Resultado: ", resultado)
    
conversor()