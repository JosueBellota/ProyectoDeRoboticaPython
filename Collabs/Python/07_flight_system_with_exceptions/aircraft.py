################################################################################
#                                                                              #
#                07 - aircraft.py (con manejo de excepciones)                  #
#                                                                              #
################################################################################

# Este fichero define la jerarquía de clases para las aeronaves.
# Es un buen ejemplo de una clase base y subclases que la especializan.

class Aircraft:
    """Clase base que representa una aeronave genérica."""
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    # --- Properties ---
    # El decorador `@property` expone un método como si fuera un atributo de solo lectura.
    @property
    def registration(self):
        return self._registration

    @property
    def model(self):
        return self._model

    def seating_plan(self):
        """Devuelve un rango de filas y una cadena de letras para los asientos."""
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


# --- Subclases ---
# Heredan de `Aircraft` y especifican valores concretos para un tipo de avión.

class AirbusA319(Aircraft):
    """Subclase para el modelo específico Airbus A319."""
    def __init__(self, registration):
        # Llama al constructor de la clase padre con valores fijos.
        super().__init__(registration, "Airbus A319", num_rows=22, num_seats_per_row=6)


class Boeing777(Aircraft):
    """Subclase para el modelo específico Boeing 777."""
    def __init__(self, registration):
        super().__init__(registration, "Boeing 777", num_rows=50, num_seats_per_row=10)
