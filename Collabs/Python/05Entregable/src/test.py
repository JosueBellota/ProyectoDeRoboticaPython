from Passenger import Passenger

from Aircraft import Aircraft, Airline, Airbus

def main():

    # [ ] p1 = Passenger("Jack", "Shephard", "85994003S")

    a1 = Aircraft(registration = "G-EUAH",
                model = "Airbus A319",
                num_rows = 22, 
                num_seats_per_row=6)
    
    a2 = Aircraft(registration = "G-EUAH",
                model = "Airbus A319",
                num_rows = 22, 
                num_seats_per_row=30)
    

    print(a1.get_registration())
    print(a1.get_model())
    print(a1.seating_plan())
    print(a1.num_seats())
    # print(p1.passenger_data())
    print("\n")
    print("Prueba Airline \n")
    air1 = Airline(registration="BA117", airline="British Airways")

    print(air1.get_registration())
    print(air1.get_airline())
    print(air1.seating_plan())
    print(air1.num_seats())


    print("\n")
    print("Prueba Airbus \n")
    air1 = Airbus(registration="BA117", variant="British Airways")
    
    print(air1.get_variant())
    print(air1.get_registration())
    print(air1.seating_plan())
    print(air1.num_seats())

    

main()