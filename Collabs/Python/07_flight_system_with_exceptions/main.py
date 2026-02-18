################################################################################
#                                                                              #
#                  07 - main.py (con manejo de excepciones)                    #
#                                                                              #
################################################################################

# Este fichero es el punto de entrada y demuestra cómo CAPTURAR las excepciones
# lanzadas por las clases del sistema de vuelos usando bloques `try...except`.

from aircraft import AirbusA319, Boeing777
from passenger import Passenger
from flight import Flight

def console_card_printer(passenger, flight_number, aircraft, seat):
    """Imprime una tarjeta de embarque con un formato específico en la consola."""
    output = f"| Nombre: {passenger.name} {passenger.surname} " \
             f"| Vuelo: {flight_number} "                     \
             f"| Asiento: {seat} "                           \
             f"| Aeronave: {aircraft} |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    print("\n".join(lines))

def demonstrate_invalid_creation():
    """Demuestra cómo se capturan los errores al crear un vuelo inválido."""
    print("--- 1. Demostración de Creación de Vuelo Inválida ---")
    try:
        # Este número de vuelo es incorrecto y `Flight.__init__` lanzará un ValueError.
        f_inv = Flight("INVALID1", aircraft=AirbusA319("G-EUPT"))
        print("Vuelo inválido creado (¡esto no debería pasar!)")
    except ValueError as e:
        # Aquí capturamos la excepción y mostramos un mensaje amigable.
        print(f"Error capturado al crear el vuelo: {e}")

def demonstrate_invalid_allocation(flight):
    """Demuestra la captura de errores durante la asignación de asientos."""
    print("\n--- 2. Demostración de Asignación de Asientos Inválida ---")
    p = Passenger("Test", "User", "12345678Z")
    
    # Intento 1: Asiento que no existe
    try:
        flight.allocate_passenger(p, "99Z")
    except ValueError as e:
        print(f"Error capturado (asiento inexistente): {e}")

    # Intento 2: Asiento ya ocupado
    try:
        flight.allocate_passenger(p, "1A") # Suponiendo que 1A ya está ocupado
    except ValueError as e:
        print(f"Error capturado (asiento ocupado): {e}")

def main():
    """Función principal que orquesta la simulación."""
    # --- Creación de Vuelos Válidos ---
    f1 = Flight("BA748", AirbusA319("G-EUPT"))
    f2 = Flight("AF120", Boeing777("F-GSPS"))

    # --- Asignación de Pasajeros Válida ---
    p1 = Passenger("Jack", "Shephard", "85994003S")
    p2 = Passenger("Kate", "Austen", "12589756P")
    p3 = Passenger("James", "Ford", "56278665F")
    f1.allocate_passenger(p1, "1A")
    f1.allocate_passenger(p2, "2B")
    f1.allocate_passenger(p3, "3C")
    
    # --- Demostración de Errores Controlados ---
    demonstrate_invalid_creation()
    demonstrate_invalid_allocation(f1)
    
    # --- Flujo Normal del Programa ---
    print("\n--- 3. Tarjetas de Embarque del Vuelo Válido ---")
    f1.make_boarding_cards(console_card_printer)
    
    print(f"\nAsientos disponibles en {f1.number()}: {f1.num_available_seats()}")

if __name__ == "__main__":
    main()
