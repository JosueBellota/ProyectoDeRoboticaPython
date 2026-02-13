from aircraft import Aircraft, Airbus, Boeing
from passenger import Passenger
from flight import Flight

def make_flights():
    """
    Crea y configura una serie de vuelos con pasajeros asignados.

    Returns:
        tuple: Una tupla que contiene las instancias de Flight f1, f2 y f3.
    """
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
    print("--- Demostración de la gestión de excepciones en el sistema de vuelos ---")

    # Ejemplo de validación del número de vuelo (en Flight.__init__)
    try:
        invalid_flight = Flight(number="ba117", aircraft=Aircraft(registration="X", model="Y", num_rows=1, num_seats_per_row=1))
    except ValueError as e:
        print(f"
Error al crear un vuelo con número inválido: {e}")

    try:
        invalid_flight = Flight(number="B117", aircraft=Aircraft(registration="X", model="Y", num_rows=1, num_seats_per_row=1))
    except ValueError as e:
        print(f"
Error al crear un vuelo con número inválido: {e}")

    try:
        invalid_flight = Flight(number="BA10000", aircraft=Aircraft(registration="X", model="Y", num_rows=1, num_seats_per_row=1))
    except ValueError as e:
        print(f"
Error al crear un vuelo con número inválido: {e}")

    f1, f2, f3 = make_flights()

    print("
--- Flight 1 Seating ---")
    f1.print_seating()
    print("
--- Flight 1 Boarding Cards ---")
    f1.print_boarding_cards()

    # Ejemplo de validación de asiento (en __parse_seat y allocate_passenger)
    try:
        print("
Intentando asignar a un asiento inválido (fila fuera de rango):")
        f1.allocate_passenger("25A", Passenger("Bad", "Seat", "123").passenger_data())
    except ValueError as e:
        print(f"Error de asignación: {e}")

    try:
        print("
Intentando asignar a un asiento inválido (letra inválida):")
        f1.allocate_passenger("12Z", Passenger("Bad", "Letter", "456").passenger_data())
    except ValueError as e:
        print(f"Error de asignación: {e}")

    try:
        print("
Intentando asignar a un asiento ya ocupado:")
        f1.allocate_passenger("12A", Passenger("Occupied", "Seat", "789").passenger_data())
    except ValueError as e:
        print(f"Error de asignación: {e}")

    # Ejemplo de validación de reasignación
    try:
        print("
Intentando reasignar desde un asiento vacío:")
        f1.reallocate_passenger("10A", "10B")
    except ValueError as e:
        print(f"Error de reasignación: {e}")

    print(f"
Available seats on Flight 1: {f1.num_available_seats()}")

    print("
--- Reallocating passenger on Flight 1 ---")
    try:
        f1.reallocate_passenger("12A", "1A")
        print("
Reasignación exitosa de 12A a 1A.")
    except ValueError as e:
        print(f"Error de reasignación: {e}")
    f1.print_seating()
    f1.print_boarding_cards()

    print(f"
Available seats on Flight 1 after reallocation: {f1.num_available_seats()}")

    print("
--- Flight 2 Seating ---")
    f2.print_seating()
    print("
--- Flight 3 Seating ---")
    f3.print_seating()
