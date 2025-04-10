#PRINCIPIO DE INVERSION DE DEPENDECIAS
#este principio nos dice que las abastracciones no deben de depender de los detalles. Los detalles son los que deberian de depender de las abstracciones

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
       #logica para verificar palabra si esta en el diccionario
       pass
   
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #usamos el verificador para corregir el texto
        pass
    
corrector = CorrectorOrtografico(Diccionario())
