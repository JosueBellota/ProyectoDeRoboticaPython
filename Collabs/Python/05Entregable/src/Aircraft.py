from pprint import pprint

class Aircraft:
    """Class representing an aircraft"""

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        if num_seats_per_row > 26:
            raise ValueError("The number of seats per row cannot be more than 26.")
        
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """Returns the registration string of the aircraft"""
        return self.__registration

    def get_model(self):
        """Returns the model name of the aircraft"""
        return self.__model

    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
        Returns:
        rows: A list of Nones (size num_rows + 1).
        seats: A string of letters such as "ABCDEF"
        """
        seat_letters = "".join(chr(65 + i) for i in range(self.__num_seats_per_row))
        rows = [None] * (self.__num_rows + 1)
        return rows, seat_letters

    def num_seats(self):
        """Calculates the total number of seats
        Returns:
        The number of seats
        """
        return self.__num_rows * self.__num_seats_per_row


class Boeing(Aircraft):
    """Class representing a Boeing aircraft"""
    __model = "Boeing 777"
    __num_rows = 56
    __num_seats_per_row = 9

    def __init__(self, registration, airline):
        super().__init__(
            registration,
            model=Boeing.__model,
            num_rows=Boeing.__num_rows,
            num_seats_per_row=Boeing.__num_seats_per_row
        )
        self.__airline = airline

    def get_airline(self):
        """Returns the name of the airline operating this Boeing"""
        return self.__airline


class Airbus(Aircraft):
    """Class representing an Airbus aircraft"""
    __model = "Airbus A319"
    __num_rows = 23
    __num_seats_per_row = 6

    def __init__(self, registration, variant):
        super().__init__(
            registration,
            model=Airbus.__model,
            num_rows=Airbus.__num_rows,
            num_seats_per_row=Airbus.__num_seats_per_row
        )
        self.__variant = variant

    def get_variant(self):
        """Returns the specific variant of this Airbus"""
        return self.__variant
