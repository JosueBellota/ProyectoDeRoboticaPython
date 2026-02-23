from Aircraft import Aircraft, Airline, Airbus


class Flight(Aircraft):

    __number = str
    __aircraft = Aircraft
    __seating = list


    

    def __init__(self, nombre, aircraft):
        self.__nombre = nombre
        
        # Guardamos la instancia de la otra clase como atributo privado
        if isinstance(aircraft, Aircraft):
            self.__aircraft = aircraft
        else:
            print("Error: El parámetro debe ser una instancia de la clase Aircraft")

    def __defining_seating(self):

        row = {}

        tupla = Aircraft.seating_plan()

        for i in range(len(tupla[0])):
            
            for i in range(len(tupla[1])):

                self.__seating.insert(i, row)
            



    def get_number():

        """Allocate a seat to a passenger
        Args:
        seat: A seat designator such as '12C' or '21F'
        passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """

    def get_aircraft_model():

        """ Reallocate a passenger to a different seat
        Args:
        from_seat: The existing seat designator for the passenger such as '12C'
        to_seat: The new seat designator
        """

    def allocate_passenger():

        """ Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """

    def reallocate_passenger():

        """ Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """

    def num_available_seats():

        """ Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """

    def print_seating():

        """Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """

    def print_boarding_cards():

        """Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """
    def __parse_seat():

        """Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """
    def __pasenger_seats():

        """Obtains the amount of unoccupied seats
        Returns:
        The number of unoccupied seats  
        """