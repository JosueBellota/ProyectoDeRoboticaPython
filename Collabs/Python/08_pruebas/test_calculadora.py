################################################################################
#                                                                              #
#                       08 - test_calculadora.py                               #
#                                                                              #
################################################################################

# Este fichero demuestra cómo escribir tests unitarios en Python usando el
# módulo `unittest`, que viene incluido por defecto.

import unittest
from calculadora import sumar, restar, dividir

# --- 1. Creación de una Clase de Tests ---
# Los tests se agrupan en clases que heredan de `unittest.TestCase`.
class TestCalculadora(unittest.TestCase):

    # --- 2. Métodos de Test ---
    # Cada test individual es un método cuyo nombre empieza por `test_`.
    def test_sumar(self):
        """Prueba la función de sumar con valores positivos, negativos y cero."""
        print("Ejecutando test_sumar...")
        # `assertEqual` comprueba si dos valores son iguales.
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-5, -5), -10)

    def test_restar(self):
        """Prueba la función de restar."""
        print("Ejecutando test_restar...")
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(5, 5), 0)

    def test_dividir(self):
        """Prueba la función de dividir, incluyendo el caso de división por cero."""
        print("Ejecutando test_dividir...")
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-8, 4), -2)
        
        # --- 3. Probar Excepciones ---
        # `assertRaises` es un "context manager" que comprueba si una operación
        # lanza la excepción esperada. El test pasa si la excepción ocurre.
        with self.assertRaises(ValueError):
            dividir(10, 0)

# --- 4. Ejecución de los Tests ---
# Este bloque permite ejecutar los tests directamente desde la línea de comandos
# con `python test_calculadora.py`.
if __name__ == '__main__':
    # `unittest.main()` descubre y ejecuta los tests en este fichero.
    unittest.main()
