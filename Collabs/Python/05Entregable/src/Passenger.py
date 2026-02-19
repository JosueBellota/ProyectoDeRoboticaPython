
class Passenger:

    __name = str
    __surname = str
    __id_card = str

    def __init__(self, name, surname, id_card):

        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):

        """Allocate a seat to a passenger
        Args:
        seat: A seat designator such as '12C' or '21F'
        passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
        # type: () -> Tuple[str, str, str]
        return (self.__name, self.__surname, self.__id_card)




