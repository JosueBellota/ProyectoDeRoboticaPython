################################################################################
#                                                                              #
#                        03_01_functions.py                                    #
#                                                                              #
################################################################################

# ---------------------- Definición básica de una función ----------------------
def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

numeros = [1, 5, 3, 2]
resultado = media(numeros)
print(f"La media de {numeros} es {resultado}")


# ---------------- Parámetros opcionales (con valores por defecto) ---------------
def saludar(nombre="Pepe", edad=None):
    mensaje = f"Hola {nombre}"
    if edad is not None:
        mensaje += f", tienes {edad} años"
    return mensaje

print(saludar())
print(saludar("Juan", 25))


# ----------------- Keyword Arguments (parámetros por nombre) ------------------
# Se pueden pasar los argumentos por nombre para cambiar su orden.
print(saludar(edad=30, nombre="Maria"))


# ---------------------- Modificación de objetos mutables ----------------------
# Los cambios en objetos mutables (listas, diccionarios) dentro de una
# función afectan al objeto original.
def modificar_lista(lista_a_modificar):
    lista_a_modificar.sort()
    if len(lista_a_modificar) > 2:
        lista_a_modificar[2] = 99
    return lista_a_modificar

mi_lista = [5, 2, 7, 4]
print("\nLista antes de modificar:", mi_lista)
modificar_lista(mi_lista)
print("Lista después de modificar:", mi_lista)


# -------------------- Parámetros arbitrarios posicionales (*args) --------------------
# La función recibe los argumentos como una tupla.
def listar_elementos(*args):
    print("\nArgumentos recibidos (tupla *args):", args)

listar_elementos(5, 2, 7, 'a')


# -------------------- Parámetros arbitrarios por nombre (**kwargs) --------------------
# La función recibe los argumentos como un diccionario.
def mostrar_detalles_persona(**kwargs):
    print("\nArgumentos recibidos (diccionario **kwargs):", kwargs)

mostrar_detalles_persona(nombre="Ana", edad=28, ciudad="Madrid")
