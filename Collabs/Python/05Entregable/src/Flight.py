from Aircraft import Aircraft
from pprint import pprint

class Flight:
    """Class representing a flight"""

    def __init__(self, number, aircraft):
        if not isinstance(number, str):
            raise ValueError(f"Flight number must be a string, not {type(number)}")
        
        if len(number) < 3:
            raise ValueError(f"Invalid flight number format: {number}")
            
        if not number[:2].isalpha():
            raise ValueError(f"First two characters of flight number must be letters: {number}")
            
        if not number[:2].isupper():
            raise ValueError(f"First two characters of flight number must be uppercase: {number}")
            
        if not number[2:].isdigit():
            raise ValueError(f"Characters after the first two must be digits: {number}")
            
        if int(number[2:]) > 9999:
            raise ValueError(f"Flight number digit part must be 9999 or less: {number}")

        self.__number = number
        self.__aircraft = aircraft

        rows_list, seat_letters = self.__aircraft.seating_plan()
        self.__seating = [None]

        for _ in rows_list[1:]:
            row_dict = {letter: None for letter in seat_letters}
            self.__seating.append(row_dict)

    def get_number(self):
        """Returns the flight number string"""
        return self.__number

    def get_aircraft_model(self):
        """Returns the model of the aircraft assigned to this flight"""
        return self.__aircraft.get_model()

    def get_seating(self):
        """Returns the current seating allocation list of dictionaries"""
        return self.__seating

    def allocate_passenger(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
        seat: A seat designator such as '12C' or '21F'
        passenger: The passenger data tuple
        """
        row, letter = self._parse_seat(seat)

        if self.__seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied")

        self.__seating[row][letter] = passenger

    def reallocate_passenger(self, from_seat, to_seat):
        """Reallocate a passenger to a different seat
        Args:
        from_seat: The current seat designator
        to_seat: The new seat designator
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self.__seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger at seat {from_seat} to reallocate")

        passenger = self.__seating[from_row][from_letter]
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self.__seating[to_row][to_letter] is not None:
            raise ValueError(f"Destination seat {to_seat} is already occupied")

        self.__seating[to_row][to_letter] = passenger
        self.__seating[from_row][from_letter] = None

    def num_available_seats(self):
        """Obtains the amount of unoccupied seats"""
        count = 0
        for row in self.__seating[1:]:
            for seat in row.values():
                if seat is None:
                    count += 1
        return count

    def print_seating(self):
        """Prints the seating plan in the console"""
        pprint(self.__seating)

    def print_boarding_cards(self):
        """Prints boarding cards for each passenger"""
        for passenger, seat in self._passenger_seats():
            name, surname, id_card = passenger
            card = f"""
| {name} {surname} {id_card} {seat} {self.get_number()} {self.get_aircraft_model()} |
"""
            print(card)

    def _parse_seat(self, seat):
        """Divide a seat designator into row and letter
        Args:
        seat: A seat designator like '12C'
        Returns: (row, letter)
        """
        _, seat_letters = self.__aircraft.seating_plan()
        
        letter = seat[-1]
        if letter not in seat_letters:
             raise ValueError(f"Invalid seat letter {letter} for this aircraft")
        
        row_str = seat[:-1]
        if not row_str.isdigit():
            raise ValueError(f"Row part of seat {seat} must be numeric")
            
        row = int(row_str)
        if row < 1 or row >= len(self.__seating):
            raise ValueError(f"Invalid row number {row} for this aircraft")
            
        return row, letter

    def _passenger_seats(self):
        """A generator function to iterate the occupied seating locations"""
        for row_index, row_dict in enumerate(self.__seating):
            if row_dict is None:
                continue
            for letter, passenger in row_dict.items():
                if passenger is not None:
                    yield passenger, f"{row_index}{letter}"
