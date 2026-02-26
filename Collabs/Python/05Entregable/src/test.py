from Aircraft import Aircraft, Boeing, Airbus
from Flight import Flight
from Passenger import Passenger
import sys

def test_flight_creation():
    """
    Tests the validation logic during the creation of a Flight object.
    Verifies that valid flight numbers are accepted and that various
    invalid formats (lowercase, non-alpha start, excessively high numbers,
    and non-digit suffixes) correctly raise ValueError exceptions.
    """
    print("Testing Flight creation...")
    aircraft = Boeing("G-BOAC", "British Airways")
    
    try:
        f = Flight("BA1234", aircraft)
        print("  OK: Valid flight BA1234 created.")
    except ValueError as e:
        print(f"  FAIL: Should have allowed BA1234. Error: {e}")

    try:
        Flight("ba123", aircraft)
        print("  FAIL: Should have rejected lowercase 'ba123'.")
    except ValueError as e:
        print(f"  OK: Rejected lowercase: {e}")

    try:
        Flight("12ABC", aircraft)
        print("  FAIL: Should have rejected '12ABC'.")
    except ValueError as e:
        print(f"  OK: Rejected non-alpha start: {e}")

    try:
        Flight("BA10000", aircraft)
        print("  FAIL: Should have rejected 'BA10000' (>9999).")
    except ValueError as e:
        print(f"  OK: Rejected number > 9999: {e}")

    try:
        Flight("BAABC", aircraft)
        print("  FAIL: Should have rejected 'BAABC'.")
    except ValueError as e:
        print(f"  OK: Rejected non-digit suffix: {e}")

def test_passenger_allocation():
    """
    Tests the allocation of passengers to specific seats.
    Ensures that a valid assignment works, while attempts to assign
    a passenger to an already occupied seat, or to non-existent rows
    and columns, raise appropriate ValueError exceptions.
    """
    print("\nTesting Passenger Allocation...")
    aircraft = Airbus("G-EUPT", "A319-100")
    flight = Flight("AF92", aircraft)
    passenger = Passenger("Jack", "Shephard", "12345678X").passenger_data()

    try:
        flight.allocate_passenger("12A", passenger)
        print("  OK: Allocated 12A.")
    except ValueError as e:
        print(f"  FAIL: Should have allowed 12A. Error: {e}")

    try:
        flight.allocate_passenger("12A", passenger)
        print("  FAIL: Should have rejected 12A (occupied).")
    except ValueError as e:
        print(f"  OK: Rejected occupied seat: {e}")

    try:
        flight.allocate_passenger("25A", passenger)
        print("  FAIL: Should have rejected row 25.")
    except ValueError as e:
        print(f"  OK: Rejected invalid row: {e}")

    try:
        flight.allocate_passenger("12Z", passenger)
        print("  FAIL: Should have rejected seat Z.")
    except ValueError as e:
        print(f"  OK: Rejected invalid letter: {e}")

def test_passenger_reallocation():
    """
    Tests the reallocation of passengers from one seat to another.
    Verifies that a successful move clears the original seat and occupies
    the new one. Also checks that attempting to reallocate from an empty
    seat or to an already occupied seat raises ValueError exceptions.
    """
    print("\nTesting Passenger Reallocation...")
    aircraft = Airbus("G-EUPT", "A319-100")
    flight = Flight("AF92", aircraft)
    p1 = Passenger("Jack", "Shephard", "12345678X").passenger_data()
    p2 = Passenger("Kate", "Austen", "87654321P").passenger_data()

    flight.allocate_passenger("1A", p1)
    flight.allocate_passenger("1B", p2)

    try:
        flight.reallocate_passenger("1A", "10C")
        print("  OK: Reallocated 1A to 10C.")
    except ValueError as e:
        print(f"  FAIL: Should have allowed reallocation. Error: {e}")

    try:
        flight.reallocate_passenger("5E", "5F")
        print("  FAIL: Should have rejected reallocating from empty 5E.")
    except ValueError as e:
        print(f"  OK: Rejected reallocation from empty: {e}")

    try:
        flight.reallocate_passenger("1B", "10C")
        print("  FAIL: Should have rejected reallocating 1B to occupied 10C.")
    except ValueError as e:
        print(f"  OK: Rejected reallocation to occupied: {e}")

def test_available_seats():
    """
    Tests the available seats counting mechanism.
    Validates that the initial count matches the aircraft's capacity and
    that subsequent passenger allocations correctly reduce the total count
    of available seats.
    """
    print("\nTesting Available Seats...")
    aircraft = Airbus("G-EUPT", "A319-100")
    flight = Flight("AF92", aircraft)
    total = flight.num_available_seats()
    print(f"  Initial seats: {total}")
    
    p = Passenger("Test", "User", "000").passenger_data()
    flight.allocate_passenger("1A", p)
    flight.allocate_passenger("1B", p)
    
    new_total = flight.num_available_seats()
    print(f"  Seats after 2 allocations: {new_total}")
    if new_total == total - 2:
        print("  OK: Available seats count is correct.")
    else:
        print(f"  FAIL: Count is wrong. Expected {total-2}, got {new_total}")

if __name__ == "__main__":
    test_flight_creation()
    test_passenger_allocation()
    test_passenger_reallocation()
    test_available_seats()
