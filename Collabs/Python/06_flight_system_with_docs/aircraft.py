import string

class Aircraft:
    """
    Representación de una aeronave.

    Attributes:
        registration (str): El registro de la aeronave.
        model (str): El modelo de la aeronave.
        num_rows (int): Número de filas de asientos.
        num_seats_per_row (int): Número de asientos por fila.
    """
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        Inicializa una nueva aeronave.

        Args:
            registration (str): El registro de la aeronave.
            model (str): El modelo de la aeronave.
            num_rows (int): Número de filas de asientos.
            num_seats_per_row (int): Número de asientos por fila.
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def __get_registration(self):
        return self.__registration

    def __get_model(self):
        return self.__model

    def __get_num_rows(self):
        return self.__num_rows

    def __get_num_seats_per_row(self):
        return self.__num_seats_per_row

    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
        Returns:
          rows: A list of Nones (size num_rows + 1).
          seats: A string of letters such as "ABCDEF"
        """
        rows = [None] + [None] * self.__num_rows
        seats = string.ascii_uppercase[:self.__num_seats_per_row]
        return rows, seats

    def num_seats(self):
        """Calculates the number of seats
        Returns:
          seats: The number of seats
        """
        return self.__num_rows * self.__num_seats_per_row

    # Getters
    registration = property(__get_registration)
    model = property(__get_model)
    num_rows = property(__get_num_rows)
    num_seats_per_row = property(__get_num_seats_per_row)

class Airbus(Aircraft):
    """
    Representación de una aeronave Airbus específica.

    Attributes:
        registration (str): El registro de la aeronave.
        variant (str): La variante del modelo Airbus (ej. A319-100).
    """
    def __init__(self, registration, variant):
        """
        Inicializa una nueva aeronave Airbus.

        Args:
            registration (str): El registro de la aeronave.
            variant (str): La variante del modelo Airbus.
        """
        super().__init__(registration, "Airbus " + variant, num_rows=22, num_seats_per_row=6)
        self.__variant = variant

    def __get_variant(self):
        return self.__variant

    variant = property(__get_variant)


class Boeing(Aircraft):
    """
    Representación de una aeronave Boeing específica.

    Attributes:
        registration (str): El registro de la aeronave.
        airline (str): La aerolínea asociada con la aeronave.
    """
    def __init__(self, registration, airline):
        """
        Inicializa una nueva aeronave Boeing.

        Args:
            registration (str): El registro de la aeronave.
            airline (str): La aerolínea asociada.
        """
        super().__init__(registration, "Boeing 747", num_rows=50, num_seats_per_row=10)
        self.__airline = airline

    def __get_airline(self):
        return self.__airline

    airline = property(__get_airline)
