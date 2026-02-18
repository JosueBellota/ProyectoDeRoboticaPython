from transporte import Transporte

class Auto(Transporte):
    """
    Clase hijo que representa un auto, hereda de Transporte.
    """
    # Declaración de variables privadas específicas de Auto
    __numero_puertas: int
    __tipo_combustible: str

    def __init__(self, marca: str, modelo: str, año: int, numero_puertas: int, tipo_combustible: str):
        """
        Inicializa un objeto Auto.
        """
        super().__init__(marca, modelo, año)
        self.__numero_puertas = numero_puertas
        self.__tipo_combustible = tipo_combustible

    @property
    def numero_puertas(self):
        return self.__numero_puertas

    @property
    def tipo_combustible(self):
        return self.__tipo_combustible

    def mostrar_info(self):
        """
        Muestra la información del auto, incluyendo sus atributos específicos.
        """
        info_padre = super().mostrar_info()
        return f"{info_padre}, {self.__numero_puertas} puertas, combustible: {self.__tipo_combustible}"

    def mover(self, distancia: float):
        """
        Implementación específica para mover un auto.
        """
        if self.encendido:
            return f"El auto {self.marca} {self.modelo} se está conduciendo por {distancia} km en la carretera."
        else:
            return f"No se puede mover el auto {self.marca} {self.modelo}. El motor está apagado."

    def abrir_maletero(self):
        """Abre el maletero del auto."""
        return f"El maletero del {self.marca} {self.modelo} ha sido abierto."
