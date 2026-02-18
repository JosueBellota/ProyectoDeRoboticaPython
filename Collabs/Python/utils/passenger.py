class Passenger:
    def __init__(self, name, surname, id_card):
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def __get_name(self):
        return self.__name

    def __get_surname(self):
        return self.__surname

    def __get_id_card(self):
        return self.__id_card

    def passenger_data(self):
        """Obtains the data of a passenger
        Returns:
          name: The passenger's name such as 'Jack'
          surname: The passenger's family name such as 'Shephard'
          id_card: The passenger's id card such as '85994003S'
        """
        return (self.__name, self.__surname, self.__id_card)

    # Getters
    name = property(__get_name)
    surname = property(__get_surname)
    id_card = property(__get_id_card)
