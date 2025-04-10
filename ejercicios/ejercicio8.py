#CHATBOT ANALIZADOR DE SENTIMIENTOS
#En este proyecto vamos a desarrollar una chatbot en python que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y nos responsa cual es sentimiento
#Este proyecto nos dara la oportunidad de trabajar co varios aspectos de la POO, modulos,API, analicis de datos. etc

from textblob import TextBlob

class AnalizadorDeSentimientos():
    def analizar_sentimiento(self, texto):
        analicis = TextBlob(texto)
        if analicis.sentiment.polarity > 0:
            return "positivo"
        elif analicis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"
        
        
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("Hello, mi friend?")
print(resultado)