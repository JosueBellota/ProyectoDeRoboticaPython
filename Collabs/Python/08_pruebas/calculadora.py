################################################################################
#                                                                              #
#                       08 - calculadora.py                                    #
#                                                                              #
################################################################################

# Este fichero contiene funciones simples que serán probadas desde otro fichero.

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def dividir(a, b):
    """
    Devuelve la división de a / b.
    Lanza una excepción si se intenta dividir por cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
