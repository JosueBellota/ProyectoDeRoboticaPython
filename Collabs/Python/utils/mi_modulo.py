# Este es el fichero: mi_modulo.py

"""
Este es un módulo de ejemplo que contiene una función, una clase
y un bloque __main__ para demostrar cómo funcionan las importaciones.
"""

# Una constante simple dentro del módulo
VERSION = "1.0"

# Una función simple
def saludar_modulo(nombre):
    """Saluda a alguien desde el módulo."""
    print(f"¡Hola, {nombre}! Te saluda el módulo 'mi_modulo' (Versión {VERSION}).")

# Una clase simple
class Calculadora:
    """Una clase de ejemplo para ser importada."""
    def sumar(self, a, b):
        return a + b

# El siguiente bloque de código solo se ejecutará si este fichero
# (mi_modulo.py) es ejecutado directamente. No se ejecutará si
# el módulo es importado desde otro fichero.
if __name__ == "__main__":
    print("--- Has ejecutado mi_modulo.py directamente ---")
    print("Este mensaje no aparecerá cuando importes este módulo.")
    saludar_modulo("Usuario de prueba")
    calc = Calculadora()
    print(f"Prueba de la calculadora: 5 + 3 = {calc.sumar(5, 3)}")
