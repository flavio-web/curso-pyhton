
#ENCAPCULAR: significa que existen atributos o metodos que solo pueden ser accedidos desde el interior de la clase pero no desde afuera y se utiliza un doble guion bajo
class MiClase:
    def __init__(self):
        #la manera de decirle que es una tributo privado con el guion bajo pero aun asi se puede acceder desde afuera de la clase
        self._atributo_privado = "valor privado"
        #manera de decirle que es un atributo privado y no se puede acceder desde afeura de la clase
        self.__atributo_muy_privado = "valor muy privado"
        
    def __metodoMuyPrivado(self):
        print("este es un metodo que solo se accede desde adentro de la clase")
        
        
        
        
objeto = MiClase()
print(objeto._atributo_privado)

#va a dar un error de acceso
#print(objeto.__atributo_muy_privado)

#no se puede acceder a este metodo porque es muy privado
#print(objeto.__metodoMuyPrivado())
        