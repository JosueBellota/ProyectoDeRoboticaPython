################################################################################
#                                                                              #
#             05_04_instance_class_static_methods.py                           #
#                                                                              #
################################################################################

# En Python, los métodos de una clase pueden ser de tres tipos.

from datetime import date

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # --- 1. Método de Instancia ---
    # El método más común. Recibe la instancia (`self`) como primer argumento.
    # Puede modificar el estado del objeto (sus atributos).
    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")

    # --- 2. Método de Clase (@classmethod) ---
    # Se decora con `@classmethod`. Recibe la clase (`cls`) como primer argumento.
    # No puede modificar el estado de una instancia específica (no tiene `self`).
    # Se usa a menudo para crear "factories" (constructores alternativos).
    @classmethod
    def desde_anyo_nacimiento(cls, nombre, anyo):
        """Constructor alternativo que crea un Empleado desde el año de nacimiento."""
        edad_calculada = date.today().year - anyo
        # `cls` aquí es la clase `Empleado`. Llamar a `cls(...)` es como
        # llamar a `Empleado(...)`.
        return cls(nombre, edad_calculada)

    # --- 3. Método Estático (@staticmethod) ---
    # Se decora con `@staticmethod`. No recibe ni `self` ni `cls`.
    # Es como una función normal, pero vive dentro del "espacio de nombres" de la clase.
    # No puede modificar el estado de la clase ni de la instancia.
    # Se usa para funcionalidades que lógicamente pertenecen a la clase pero no
    # dependen de su estado.
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


# --- Prueba de Método de Instancia ---
print("--- 1. Método de Instancia ---")
e1 = Empleado("Ana", 25)
e1.presentarse()


# --- Prueba de Método de Clase (Factory) ---
print("\n--- 2. Método de Clase ---")
# Usamos el método de clase como un constructor alternativo.
e2 = Empleado.desde_anyo_nacimiento("Pedro", 1995)
e2.presentarse()


# --- Prueba de Método Estático ---
print("\n--- 3. Método Estático ---")
# Se puede llamar desde la clase directamente, sin necesidad de crear una instancia.
print(f"¿Es mayor de edad (20)? {Empleado.es_mayor_de_edad(20)}")
print(f"¿Es mayor de edad (17)? {Empleado.es_mayor_de_edad(17)}")
