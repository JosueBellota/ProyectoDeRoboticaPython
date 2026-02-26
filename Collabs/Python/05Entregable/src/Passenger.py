
class Passenger:
    """Class representing a passenger"""

    def __init__(self, name, surname, id_card):
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):
        """Obtains the data of a passenger as a tuple (name, surname, id_card)"""
        return (self.__name, self.__surname, self.__id_card)
