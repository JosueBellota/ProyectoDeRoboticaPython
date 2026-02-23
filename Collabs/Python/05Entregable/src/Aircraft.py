# from pprint import pprint

# pprint(seating)

class Aircraft:
    """ Creamos una nueva persona con un nombre y una edad """

# texto
    __registration = str 

# mnumero
    __model = str
# lista
    __nun_rows = int
# diccionario
    __num_seats_per_row = int


    def __init__(self, registration, model, num_rows, num_seats_per_row):

        # supera el limite del abecedario 
        if(num_seats_per_row > 26):
            
            print("the numbers of seat per row cannot be more than 26 ")
        else:
            self.__registration = registration
            self.__model  = model
            self.__num_rows = num_rows
            self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):

        """Calculates the number of seats
        Returns:
        seats: The number of seats
        """

        return(self.__registration)

    def get_model(self):

        """Calculates the number of seats
        Returns:
        seats: The number of seats
        """

        return(self.__model)
        


    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
        Returns:
        rows: A list of Nones (size num_rows + 1).
        seats: A string of letters such as "ABCDEF"
        """

        caracteres = []
        # alfabeto ingles
        # Mayúsculas	A	65
        # Minúsculas	a	97
        for i in range(65, 65 + self.__num_seats_per_row):

            caracteres.append(chr(i))
        
        letters = "".join(caracteres)

        return(self.__num_rows, letters)
            

       
    def num_seats(self):
        """Calculates the number of seats
        Returns:
        seats: The number of seats
        """
        
        number_of_seats = self.__num_rows * self.__num_seats_per_row

        return(number_of_seats)

class Airline(Aircraft):

    __model = "Boeing 777"
    __num_rows = 56
    __num_seats_per_row = 9
    __airline = str

    def __init__(self, registration, airline):
 

        # llamando al constructor del padre para que rellene tus datos usa los parametro privados de airline en vez de los por defecto.
        super().__init__(
            registration, 
            model = Airline.__model,
            num_rows =  Airline.__num_rows, 
            num_seats_per_row = Airline.__num_seats_per_row)

        self.__airline = airline
       
        
    def get_airline(self):

        return self.__airline





class Airbus(Aircraft):

    __model = "Airbus A319"
    __num_rows = 56
    __num_seats_per_row = 9
    __variant = str

    def __init__(self, registration, variant):

   
        # llamando al constructor del padre para que rellene tus datos usa los parametro privados de airline en vez de los por defecto.
        super().__init__(
            registration, 
            model = Airbus.__model,
            num_rows =  Airbus.__num_rows, 
            num_seats_per_row = Airbus.__num_seats_per_row)

        self.__variant  = variant
        
    def get_variant(self):

        return self.__variant
