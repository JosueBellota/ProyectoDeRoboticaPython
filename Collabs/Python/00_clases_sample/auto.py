from transporte import Transporte

class Auto(Transporte):
    """
    Clase hijo que representa un auto, hereda de Transporte.
    """
    def __init__(self, marca, modelo, año, numero_puertas, tipo_combustible):
        """
        Inicializa un objeto Auto.

        Args:
            marca (str): La marca del auto.
            modelo (str): El modelo del auto.
            año (int): El año de fabricación del auto.
            numero_puertas (int): El número de puertas del auto.
            tipo_combustible (str): El tipo de combustible que utiliza el auto.
        """
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.tipo_combustible = tipo_combustible

    def mostrar_info(self):
        """
        Muestra la información del auto, incluyendo sus atributos específicos.
        (Polimorfismo - sobreescritura de método)
        """
        info_padre = super().mostrar_info()
        return f"{info_padre}, {self.numero_puertas} puertas, combustible: {self.tipo_combustible}"

    def mover(self, distancia):
        """
        Implementación específica para mover un auto.
        (Polimorfismo - implementación de método)
        """
        if self.encendido:
            return f"El auto {self.marca} {self.modelo} se está conduciendo por {distancia} km en la carretera."
        else:
            return f"No se puede mover el auto {self.marca} {self.modelo}. El motor está apagado."

    def abrir_maletero(self):
        """Abre el maletero del auto."""
        return f"El maletero del {self.marca} {self.modelo} ha sido abierto."
