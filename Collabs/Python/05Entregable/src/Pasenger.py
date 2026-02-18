
class Pasenger:

    __name = None
    __surname = None
    __id_card = None

    def __init__(self, name, surname, id_card):
        self.name = name
        self.surname = surname
        self.id_card = id_card

    def passenger_data():

        """Allocate a seat to a passenger
        Args:
        seat: A seat designator such as '12C' or '21F'
        passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
