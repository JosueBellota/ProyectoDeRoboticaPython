from transporte import Transporte

class Moto(Transporte):
    """
    Clase hijo que representa una motocicleta, hereda de Transporte.
    """
    # Declaración de variables privadas específicas de Moto
    __cilindrada: int
# pero antes de hacer mis cosas, ve a la clase padre (Transporte) y ejecuta su constructor usando estos datos
    def __init__(self, marca: str, modelo: str, año: int, cilindrada: int):
        """
        Inicializa un objeto Moto.
        """
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    def mostrar_info(self):
        """
        Muestra la información de la moto, incluyendo sus atributos específicos.
        """
        info_padre = super().mostrar_info()
        return f"{info_padre}, Cilindrada: {self.__cilindrada}cc"

    def mover(self, distancia: float):
        """
        Implementación específica para mover una moto.
        """
        if self.encendido:
            return f"La moto {self.marca} {self.modelo} está rodando por {distancia} km."
        else:
            return f"No se puede mover la moto {self.marca} {self.modelo}. El motor está apagado."

    def hacer_wheelie(self):
        """Realiza un truco con la moto."""
        return f"¡La {self.marca} {self.modelo} está haciendo un wheelie!"
