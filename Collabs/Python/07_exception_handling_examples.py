"""
Este módulo contiene ejemplos de gestión y propagación de excepciones en Python,
basado en el cuaderno "07_Gestión_de_excepciones.ipynb".
"""

# 1.1 Captura de excepciones (try-except-else-finally)

def ejemplo_captura_basica():
    """Demuestra el uso básico de try-except para capturar un IndexError."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo de Captura Básica ---")
    print("inicio")
    try:
        print(lista[4])
    except:
        print("se ha producido una excepción")
    print("fin")
    print("-" * 30)

def ejemplo_try_else():
    """Demuestra el uso de try-except-else."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo con else ---")
    print("inicio")
    try:
        # Intentará acceder a lista[4] (fuera de rango)
        # print(lista[4])
        # Para probar el 'else', comentar la línea anterior y descomentar la siguiente
        print(lista[0])
    except:
        print("se ha producido una excepción")
    else:
        print("este fin se muestra si no se produce excepción")
    print("-" * 30)

def ejemplo_try_finally():
    """Demuestra el uso de try-except-finally."""
    def mostrar_elemento():
        lista = [4, 5, 1, 3]
        print("inicio de la función")
        try:
            print(lista[4])
        except:
            print("se ha producido una excepción")
            return -1
        else:
            print("este fin se muestra si no se produce excepción")
        finally:
            print("el código del finally se ejecuta siempre")
        print("fin de la función")
        return 1

    print("--- Ejemplo con finally ---")
    mostrar_elemento()
    print("-" * 30)

# 1.2 Múltiples excepciones

def ejemplo_multiples_excepciones_tupla():
    """Demuestra la captura de múltiples excepciones usando una tupla."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo Múltiples Excepciones (Tupla) ---")
    print("inicio")
    try:
        # Genera IndexError
        print(lista[4])
        # Genera RuntimeError (si lo descomentamos y comentamos la anterior)
        # raise RuntimeError("Un error en tiempo de ejecución")
    except (RuntimeError, IndexError) as err:
        print(f"se ha producido una excepción: {err}")
        print(f"esta excepción es de tipo {type(err).__name__}")
    print("fin")
    print("-" * 30)

def ejemplo_multiples_excepciones_separadas():
    """Demuestra la captura de múltiples excepciones con except separados."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo Múltiples Excepciones (Separadas) ---")
    print("inicio")
    try:
        print(lista[4])
    except RuntimeError:
        print("Hacemos una cosa para RuntimeError")
    except IndexError:
        print("Hacemos otra cosa para IndexError")
    print("fin")
    print("-" * 30)

def ejemplo_jerarquia_excepciones():
    """Demuestra la captura de excepciones base (BaseException)."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo Jerarquía de Excepciones (BaseException) ---")
    print("inicio")
    try:
        print(lista[4])
    except BaseException as err:
        print(f"se ha producido una excepción: {err}")
        print(f"esta excepción es de tipo {type(err).__name__}")
    print("fin")
    print("-" * 30)

def ejemplo_orden_excepciones():
    """Demuestra la importancia del orden al capturar excepciones."""
    lista = [4, 5, 1, 3]
    print("--- Ejemplo Orden de Excepciones ---")
    print("inicio")
    try:
        print(lista[4])
    except IndexError:
        print("Entramos por el except de IndexError (más específico)")
    except BaseException:
        print("Este bloque de código es inalcanzable si IndexError ocurre primero")
    print("fin")
    print("-" * 30)

# 1.3 Propagación de excepciones (raise)

def ejemplo_propagacion_directa(lista, pos):
    """Función que maneja la excepción internamente (no la propaga)."""
    print("--- Ejemplo Propagación (Manejo Interno) ---")
    try:
        print(lista[pos])
    except IndexError:
        print("La posición está fuera de rango (manejado en la función)")

def ejemplo_propagacion_raise(lista, pos):
    """Función que propaga la excepción usando raise."""
    print("--- Ejemplo Propagación (Usando raise) ---")
    if (pos >= 0 and pos < len(lista)) or (pos < 0 and abs(pos) <= len(lista)):
        print(lista[pos])
    else:
        raise IndexError("La posición está fuera de rango (excepción propagada)")

if __name__ == "__main__":
    ejemplo_captura_basica()
    ejemplo_try_else()
    ejemplo_try_finally()
    ejemplo_multiples_excepciones_tupla()
    ejemplo_multiples_excepciones_separadas()
    ejemplo_jerarquia_excepciones()
    ejemplo_orden_excepciones()

    # Ejemplo de propagación
    lista_main = [4, 5, 1, 3]
    print("
--- Demostración de Propagación de Excepciones ---")
    print("inicio del main para propagación")

    ejemplo_propagacion_directa(lista_main, 4) # La excepción se maneja dentro de la función

    try:
        ejemplo_propagacion_raise(lista_main, -5) # La excepción se propaga y se captura en el main
    except IndexError as e:
        print(f"Capturado en el main: {e}")

    print("fin del main para propagación")
    print("-" * 30)