#el principio nos dice que tiene estar abierta a extensiones pero cerrada a modificaciones. es decir que se puede agregar mas funcionalidades pero no se puede modificar el codigo ya existente.
class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Eneviando mensaje por EMAIL a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Eneviando mensaje por SMS a {self.usuario.sms}")
        
class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Eneviando mensaje por WhatsApp a {self.usuario.whatsapp}")