#El princpio de sustitucion de Liskov
## Este principio nos dice que todo lo que una subclase herede de una clase, debe poder implementarlo

""" class Ave:
    def volar(self):
        print('Estoy volando')
        
        
class Pinguino(Ave):
    def volar(self):
        print("No puedo volar")
        
def hacer_volar( ave = Ave ):
    return ave.volar()

print(hacer_volar(Pinguino())) """

#En este ejemplo no cumple con el prinicipio porque las aves Pinguinos no pueden volar, por ende tenemos que recategorizar las aves para poder implementar este princiipio
        
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass


def hacer_volar( ave = Ave ):
    return ave.volar()


print(hacer_volar(AveVoladora()))