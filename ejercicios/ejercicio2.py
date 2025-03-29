#Crear una calculadora con las operaciones bascias pero cada operacion debe estar en una funcion seperada

def suma( a = 0, b = 0):
    return a + b

def resta( a = 0, b = 0):
    return a - b

def multiplicacion( a = 0, b = 0):
    return a * b

def division( a = 0, b = 0):
    if( b != 0 ):
        return a / b
    else:
        return "Error de division"
    
    
def calculadora():
    print("**** Seleccionar una operacion ****")
    print("=====================")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    
    operacion = int(input("Ingrese el numero de la operacion: "))
    
    if( operacion < 1 or operacion > 4):
        print("Error al seleccionar operacion, vuelva a intentarlo.... ")
        calculadora()
    else:
        
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        if( operacion == 1 ):
            resultado = suma(numero1, numero2)
            print("===> El resultado de la suma es: ", resultado)
            
        elif( operacion == 2 ):
            resultado = resta(numero1, numero2)
            print("===> El resultado de la resta es: ", resultado)
            
        elif( operacion == 3 ):
            resultado = multiplicacion(numero1, numero2)
            print("===> El resultado de la multiplicacion es: ", resultado)
        else:
            resultado = division(numero1, numero2)
            print("===> El resultado de la division es: ", resultado)
            
        
        print("Desea realizar otra operacion?")
        print("(S) Si quiero realizar otra operacion")          
        print("(N) Salir del sistema") 
        
        otraOperacion = input("Ingresar respuesta: ").upper()
        
        if( otraOperacion == "N" ):
            return
        
        calculadora()
                 

calculadora()