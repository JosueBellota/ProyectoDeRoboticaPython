class Transporte:
    """
    Clase padre que representa un medio de transporte genérico.
    """
    def __init__(self, marca, modelo, año):
        """
        Inicializa un objeto de transporte.

        Args:
            marca (str): La marca del vehículo.
            modelo (str): El modelo del vehículo.
            año (int): El año de fabricación del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        """Enciende el motor del vehículo."""
        if not self.encendido:
            self.encendido = True
            return f"El motor de {self.marca} {self.modelo} está ahora encendido."
        else:
            return f"El motor de {self.marca} {self.modelo} ya estaba encendido."

    def apagar(self):
        """Apaga el motor del vehículo."""
        if self.encendido:
            self.encendido = False
            return f"El motor de {self.marca} {self.modelo} está ahora apagado."
        else:
            return f"El motor de {self.marca} {self.modelo} ya estaba apagado."

    def mostrar_info(self):
        """Muestra la información básica del vehículo."""
        return f"Vehículo: {self.año} {self.marca} {self.modelo}"

    def mover(self, distancia):
        """
        Método genérico para mover el vehículo.
        Las clases hijas deben implementar su propia lógica.
        """
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")

