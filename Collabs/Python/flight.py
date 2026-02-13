from pprint import pprint
from aircraft import Aircraft

class Flight:
    def __init__(self, number, aircraft):
        self.__number = number
        self.__aircraft = aircraft
        rows, seats_letters = self.__aircraft.seating_plan()
        self.__seating = [None] + [{letter: None for letter in seats_letters} for _ in range(1, self.__aircraft.num_rows + 1)]

    def __get_number(self):
        return self.__number

    def __get_aircraft(self):
        return self.__aircraft

    def __parse_seat(self, seat):
        """Divide a seat designator in row and letter
        Args:
          seat: The seat designator to be divided such as '12C'
        Returns:
          row: The row of the seat such as 12
          letter: The letter of the seat such as 'C'
        """
        letter = seat[-1]
        row = int(seat[:-1])
        return row, letter

    def allocate_passenger(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
          seat: A seat designator such as '12C' or '21F'
          passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
        row, letter = self.__parse_seat(seat)
        self.__seating[row][letter] = passenger

    def reallocate_passenger(self, from_seat, to_seat):
        """Reallocate a passenger to a different seat
        Args:
          from_seat: The existing seat designator for the passenger such as '12C'
          to_seat: The new seat designator
        """
        from_row, from_letter = self.__parse_seat(from_seat)
        to_row, to_letter = self.__parse_seat(to_seat)

        passenger_data = self.__seating[from_row][from_letter]
        self.__seating[from_row][from_letter] = None
        self.__seating[to_row][to_letter] = passenger_data

    def num_available_seats(self):
        """Obtains the amount of unoccupied seats
        Returns:
          The number of unoccupied seats
        """
        count = 0
        for row in self.__seating[1:]:
            for seat in row.values():
                if seat is None:
                    count += 1
        return count

    def print_seating(self):
        """Prints in console the seating plan
        Example of one row:
          {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        pprint(self.__seating)

    def __passenger_seats(self):
        """A generator function to iterate the occupied seating locations
        Returns:
          generator: Tuple of the passenger data and the seat
        """
        for row_idx, row in enumerate(self.__seating[1:], start=1):
            for seat_letter, passenger_data in row.items():
                if passenger_data is not None:
                    yield passenger_data, f"{row_idx}{seat_letter}"

    def print_boarding_cards(self):
        """Prints in console the boarding card for each passenger
        Example of one boarding card:
        ----------------------------------------------------------
        |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
        ----------------------------------------------------------
        """
        for passenger_data, seat in self.__passenger_seats():
            name, surname, id_card = passenger_data
            card_info = f"{name} {surname} {id_card} {seat} {self.__number} {self.__aircraft.model}"
            print("-" * 58)
            print(f"| {card_info.ljust(54)} |")
            print("-" * 58)

    def get_seating(self):
        return self.__seating

    # Getters
    number = property(__get_number)
    aircraft = property(__get_aircraft)
