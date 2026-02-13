# 03_01_functions.py

# Definición básica de una función
def media(lista_numeros):
    """Calcula la media de una lista
    Args: lista_numeros (list[])
    Returns: float
    """
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma / len(lista_numeros)

# Uso de la función
num = [1, 5, 3, 2]
resultado = media(num)
print(f"La media de {num} es {resultado}")

# Parámetros opcionales (con valores por defecto)
def saludar(nombre="Pepe", edad=None):
    """
    Args: nombre (str), edad (int, opcional)
    Returns: str
    """
    mensaje = f"Hola {nombre}"
    if edad is not None:
        mensaje += f", tienes {edad} años"
    return mensaje

print(saludar()) # Usa valor por defecto
print(saludar("Juan", 25)) # Sobrescribe valores

# Keyword Arguments (kwargs) - Permite cambiar el orden de los parámetros
print(saludar(edad=30, nombre="Maria"))

# Paso por referencia (objetos mutables como listas)
def modificar_lista(lista):
    lista.sort()
    if len(lista) > 2:
        lista[2] = 99
    return lista

mi_lista = [5, 2, 7, 4]
print("Antes de modificar:", mi_lista)
modificar_lista(mi_lista)
print("Después de modificar (afecta a la original):", mi_lista)

# Número arbitrario de parámetros (*args)
def listar_numeros(*args):
    """Recibe cualquier cantidad de argumentos y los trata como una tupla"""
    lista = list(args)
    lista.sort()
    print("Números ordenados:", lista)

listar_numeros(5, 2, 7, 4)
listar_numeros(10, 1, 8)
