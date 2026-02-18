from aircraft import Aircraft, Airbus, Boeing
from passenger import Passenger
from flight import Flight

def make_flights():
    f1 = Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    f2 = Flight(number = "AF92", aircraft = Boeing(registration = "F-GSPS", airline = "Emirates"))
    f3 = Flight(number = "BA148", aircraft = Airbus(registration = "G-EUPT", variant = "A319-100"))

    p1 = Passenger("Jack", "Shephard", "85994003S")
    p2 = Passenger("Kate", "Austen", "12589756P")
    p3 = Passenger("James", "Ford", "56278665F")
    p4 = Passenger("John", "Locke", "10265448H")
    p5 = Passenger("Sayid", "Jarrah", "15758664M")

    f1.allocate_passenger("12A", p1.passenger_data())
    f1.allocate_passenger("18F", p2.passenger_data())
    f1.allocate_passenger("18E", p3.passenger_data())
    f1.allocate_passenger("1C", p4.passenger_data())
    f1.allocate_passenger("4D", p5.passenger_data())

    return f1, f2, f3

if __name__ == "__main__":
    f1, f2, f3 = make_flights()
    print("--- Flight 1 Seating ---")
    f1.print_seating()
    print("\n--- Flight 1 Boarding Cards ---")
    f1.print_boarding_cards()

    print("\n--- Flight 2 Seating ---")
    f2.print_seating()
    print("\n--- Flight 3 Seating ---")
    f3.print_seating()

    print(f"\nAvailable seats on Flight 1: {f1.num_available_seats()}")

    print("\n--- Reallocating passenger on Flight 1 ---")
    f1.reallocate_passenger("12A", "1A")
    f1.print_seating()
    f1.print_boarding_cards()

    print(f"\nAvailable seats on Flight 1 after reallocation: {f1.num_available_seats()}")