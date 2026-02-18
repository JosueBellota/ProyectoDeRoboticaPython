################################################################################
#                                                                              #
#                           03_04_tuples.py                                    #
#                                                                              #
################################################################################

# Colecciones de elementos ORDENADOS e INMUTABLES (no se pueden modificar).

# --------------------------- Creación de Tuplas ---------------------------
tupla_con_parentesis = (25, 12, 14, 29, 12)
tupla_sin_parentesis = 25, 12, 14, 29

# Tupla de un solo elemento (la coma final es obligatoria).
tupla_un_elemento = (43,)

# Crear una tupla desde otra colección (ej. una lista).
tupla_desde_lista = tuple([1, 2, 3])
print("Tupla:", tupla_con_parentesis)
print("Tupla de 1 elemento:", tupla_un_elemento)


# -------------------------- Acceso y Slicing --------------------------
# Igual que las listas, usando índices.
print("\nPrimer elemento:", tupla_con_parentesis[0])
print("Último elemento:", tupla_con_parentesis[-1])
print("Slice [1:4]:", tupla_con_parentesis[1:4])


# ------------------------ Inmutabilidad de las Tuplas ------------------------
# Intentar modificar un elemento de una tupla provoca un error (TypeError).
# tupla_con_parentesis[0] = 99  # <-- Esto fallaría


# ----------------------------- Métodos de Tupla -----------------------------
# Las tuplas solo tienen métodos que no modifican su contenido.
print("\nLongitud:", len(tupla_con_parentesis))
print("Contar apariciones del 12:", tupla_con_parentesis.count(12))
print("Índice de la primera aparición del 14:", tupla_con_parentesis.index(14))


# ----------- Desempaquetado (Unpacking) y uso en funciones -----------
def calcular_operaciones(a, b):
    # Las funciones pueden devolver múltiples valores, que se empaquetan en una tupla.
    return a + b, a - b

# La tupla devuelta se puede "desempaquetar" en variables individuales.
resultado_suma, resultado_resta = calcular_operaciones(5, 3)

print(f"\nResultado de la suma (desempaquetado): {resultado_suma}")
print(f"Resultado de la resta (desempaquetado): {resultado_resta}")
