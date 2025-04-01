#Poliformismo: Es la manera de darle el mismo mensaje a diferentes objetos y se resultado sea diferente. Por ejmplo si le digo al perro que haga su sonido este ladrará pero si le digo al gato que haga su sonido este maullará.

class Gato:
    def sonido(self):
        return "Miau"
    
class Perro: 
    def sonido(self):
        return "Guau"
    
gato = Gato()
perro = Perro()

