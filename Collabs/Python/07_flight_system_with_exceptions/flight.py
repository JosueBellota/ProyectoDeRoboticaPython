################################################################################
#                                                                              #
#                 07 - flight.py (con manejo de excepciones)                   #
#                                                                              #
################################################################################

# Este fichero define la clase `Flight` y es un buen ejemplo de cómo usar
# excepciones (`raise ValueError`) para validar datos y reforzar reglas de negocio.

from aircraft import Aircraft
from passenger import Passenger

class Flight:
    """Un vuelo con un número, una aeronave y una asignación de asientos."""

    def __init__(self, number, aircraft):
        # --- Validación en el constructor ---
        if not (len(number) > 2 and number[:2].isalpha() and number[2:].isdigit()):
            raise ValueError(f"Número de vuelo inválido: '{number}'")

        if not isinstance(aircraft, Aircraft):
            raise TypeError(f"Se esperaba un objeto Aircraft, pero se recibió {type(aircraft).__name__}")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model

    def _parse_seat(self, seat):
        """Valida y descompone un designador de asiento (ej. '12C') en (fila, letra)."""
        rows, seat_letters = self._aircraft.seating_plan()
        
        letter = seat[-1].upper()
        if letter not in seat_letters:
            raise ValueError(f"Asiento inválido: la letra '{letter}' no es válida.")

        try:
            row = int(seat[:-1])
        except ValueError:
            raise ValueError(f"Asiento inválido: la fila '{seat[:-1]}' no es un número.")
            
        if row not in rows:
            raise ValueError(f"Asiento inválido: la fila '{row}' no existe.")

        return row, letter

    def allocate_passenger(self, passenger, seat):
        """Asigna un pasajero a un asiento."""
        if not isinstance(passenger, Passenger):
            raise TypeError("El pasajero debe ser un objeto de la clase Passenger.")

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"El asiento {seat} ya está ocupado.")
            
        self._seating[row][letter] = passenger

    def reallocate_passenger(self, from_seat, to_seat):
        """Reasigna un pasajero de un asiento a otro."""
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No hay pasajero en el asiento {from_seat} para reasignar.")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"El asiento de destino {to_seat} ya está ocupado.")
            
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        """Devuelve el número de asientos libres."""
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row)

    def make_boarding_cards(self, card_printer):
        """Crea las tarjetas de embarque para todos los pasajeros."""
        for passenger, seat in self._passenger_seats():
            card_printer(passenger, self.number(), self.aircraft_model(), seat)

    def _passenger_seats(self):
        """Generador que devuelve los pasajeros y sus asientos."""
        rows, seat_letters = self._aircraft.seating_plan()
        for row in rows:
            for letter in seat_letters:
                if self._seating[row][letter] is not None:
                    yield (self._seating[row][letter], f"{row}{letter}")
