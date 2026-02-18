from typing import List
from transporte import Transporte

class Dueño:
    """
    Clase que representa al dueño de un vehículo.
    """
    # Declaración de variables privadas
    __nombre: str
    __direccion: str
    __vehiculos: List[Transporte]

    def __init__(self, nombre: str, direccion: str):
        """
        Inicializa un objeto Dueño.
        """
        self.__nombre = nombre
        self.__direccion = direccion
        self.__vehiculos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @property
    def vehiculos(self):
        return self.__vehiculos

    def comprar_vehiculo(self, vehiculo: Transporte):
        """
        Añade un vehículo a la lista de vehículos del dueño.
        """
        self.__vehiculos.append(vehiculo)
        print(f"{self.__nombre} ha comprado un {vehiculo.marca} {vehiculo.modelo}.")

    def mostrar_vehiculos(self):
        """Muestra todos los vehículos que posee el dueño."""
        print(f"Vehículos de {self.__nombre}:")
        if not self.__vehiculos:
            print("No posee ningún vehículo.")
        else:
            for vehiculo in self.__vehiculos:
                print(f"- {vehiculo.mostrar_info()}")
