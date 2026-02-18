class Transporte:
    """
    Clase padre que representa un medio de transporte genérico.
    """
    # Declaración de variables privadas antes del constructor
    __marca: str
    __modelo: str
    __año: int
    __encendido: bool

    def __init__(self, marca: str, modelo: str, año: int):
        """
        Inicializa un objeto de transporte.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__encendido = False

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def año(self):
        return self.__año

    @property
    def encendido(self):
        return self.__encendido

    @encendido.setter
    def encendido(self, valor: bool):
        self.__encendido = valor

    def encender(self):
        """Enciende el motor del vehículo."""
        if not self.__encendido:
            self.__encendido = True
            return f"El motor de {self.__marca} {self.__modelo} está ahora encendido."
        else:
            return f"El motor de {self.__marca} {self.__modelo} ya estaba encendido."

    def apagar(self):
        """Apaga el motor del vehículo."""
        if self.__encendido:
            self.__encendido = False
            return f"El motor de {self.__marca} {self.__modelo} está ahora apagado."
        else:
            return f"El motor de {self.__marca} {self.__modelo} ya estaba apagado."

    def mostrar_info(self):
        """Muestra la información básica del vehículo."""
        return f"Vehículo: {self.__año} {self.__marca} {self.__modelo}"

    def mover(self, distancia: float):
        """
        Método genérico para mover el vehículo.
        """
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")
