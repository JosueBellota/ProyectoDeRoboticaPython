"""
Este módulo demuestra el uso de docstrings en Python para documentar módulos,
funciones, métodos y clases.
"""

import math

# Ejemplo de docstring de una línea para una función
def funcion_simple():
  '''Esta función devuelve True.'''
  return True

# Ejemplo de docstring de varias líneas para una función con Args y Returns
def por3(valor):
  """ Esta función devuelve el número multiplicado por 3

  Args:
    valor (int): El número que se recibe

  Returns:
    int: El número multiplicado por 3

  """
  return valor*3

# Ejemplo de docstring para una clase y sus métodos
class PersonaDocumentada:
  """
  Representación de una persona con documentación completa.

  Attributes:
    nombre (str): El nombre de la persona.
    apellido (str): El apellido de la persona.
    edad (int): La edad de la persona.

  Methods:
    mostrar_info(): Muestra los datos de la persona.

  """

  def __init__(self, nombre, apellido, edad):
    """ Inicializa una persona con sus datos

    Args:
      nombre (str): El nombre de la persona.
      apellido (str): El apellido de la persona.
      edad (int): La edad de la persona.
    """
    self.__nombre = nombre
    self.__apellido = apellido
    self.__edad = edad

  def mostrar_info(self):
    """ Muestra los datos de la persona por consola. """
    print(f"Hola, soy {self.__nombre} {self.__apellido} y tengo {self.__edad} años.")

if __name__ == "__main__":
    print("--- Demostración de docstrings ---")

    print("help(math.sqrt):")
    help(math.sqrt)
    print("math.sqrt.__doc__:", math.sqrt.__doc__)

    print("help(funcion_simple):")
    help(funcion_simple)

    print("help(por3):")
    help(por3)

    print("help(PersonaDocumentada):")
    help(PersonaDocumentada)

    p = PersonaDocumentada("Juan", "Perez", 30)
    p.mostrar_info()
    print("help(p.mostrar_info):")
    help(p.mostrar_info)

    print("help(Este módulo):")
    help(__name__)
