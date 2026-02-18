class Dueño:
    """
    Clase que representa al dueño de un vehículo.
    """
    def __init__(self, nombre, direccion):
        """
        Inicializa un objeto Dueño.

        Args:
            nombre (str): El nombre del dueño.
            direccion (str): La dirección del dueño.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.vehiculos = []

    def comprar_vehiculo(self, vehiculo):
        """
        Añade un vehículo a la lista de vehículos del dueño.

        Args:
            vehiculo (Transporte): El vehículo a añadir.
        """
        self.vehiculos.append(vehiculo)
        print(f"{self.nombre} ha comprado un {vehiculo.marca} {vehiculo.modelo}.")

    def mostrar_vehiculos(self):
        """Muestra todos los vehículos que posee el dueño."""
        print(f"Vehículos de {self.nombre}:")
        if not self.vehiculos:
            print("No posee ningún vehículo.")
        else:
            for vehiculo in self.vehiculos:
                print(f"- {vehiculo.mostrar_info()}")
