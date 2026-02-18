from transporte import Transporte

class Moto(Transporte):
    """
    Clase hijo que representa una motocicleta, hereda de Transporte.
    """
    def __init__(self, marca, modelo, año, cilindrada):
        """
        Inicializa un objeto Moto.

        Args:
            marca (str): La marca de la moto.
            modelo (str): El modelo de la moto.
            año (int): El año de fabricación de la moto.
            cilindrada (int): La cilindrada del motor en cc.
        """
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        """
        Muestra la información de la moto, incluyendo sus atributos específicos.
        (Polimorfismo - sobreescritura de método)
        """
        info_padre = super().mostrar_info()
        return f"{info_padre}, Cilindrada: {self.cilindrada}cc"

    def mover(self, distancia):
        """
        Implementación específica para mover una moto.
        (Polimorfismo - implementación de método)
        """
        if self.encendido:
            return f"La moto {self.marca} {self.modelo} está rodando por {distancia} km."
        else:
            return f"No se puede mover la moto {self.marca} {self.modelo}. El motor está apagado."

    def hacer_wheelie(self):
        """Realiza un truco con la moto."""
        return f"¡La {self.marca} {self.modelo} está haciendo un wheelie!"
