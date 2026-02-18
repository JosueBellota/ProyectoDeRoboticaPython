################################################################################
#                                                                              #
#                07 - passenger.py (con manejo de excepciones)                 #
#                                                                              #
################################################################################

# Este fichero define la clase para un Pasajero. Es una clase simple
# principalmente para contener datos.

class Passenger:
    """Un pasajero con nombre, apellido y DNI."""
    def __init__(self, name, surname, id_card):
        # La validación de datos se podría añadir aquí si fuera necesario.
        self._name = name
        self._surname = surname
        self._id_card = id_card

    # --- Properties ---
    # Exponen los atributos internos como de solo lectura.
    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def id_card(self):
        return self._id_card
        
    def __str__(self):
        """Representación en string del objeto Pasajero."""
        return f"Pasajero: {self.name} {self.surname} ({self.id_card})"
