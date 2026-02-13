# 05_04_special_methods.py
from datetime import date

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de Instancia
    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")

    # Método de Clase (@classmethod)
    # Recibe 'cls' (la clase) en lugar de 'self' (la instancia).
    # Útil para Factory Methods (crear objetos de formas distintas).
    @classmethod
    def desde_anyo_nacimiento(cls, nombre, anyo):
        edad = date.today().year - anyo
        return cls(nombre, edad)

    # Método Estático (@staticmethod)
    # No recibe ni 'self' ni 'cls'. Es una función normal dentro del namespace de la clase.
    # Útil para utilidades que no dependen del estado de la clase/instancia.
    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18

# Uso de métodos
e1 = Empleado("Ana", 25)
e1.presentarse()

# Uso de Factory Method
e2 = Empleado.desde_anyo_nacimiento("Pedro", 1995)
e2.presentarse()

# Uso de Método Estático
print(f"¿Es mayor de edad (20)? {Empleado.es_mayor_edad(20)}")
