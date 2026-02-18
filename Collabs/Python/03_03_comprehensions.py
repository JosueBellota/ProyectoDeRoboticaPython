################################################################################
#                                                                              #
#                       03_03_comprehensions.py                                #
#                                                                              #
################################################################################

# Forma concisa de crear colecciones (listas, diccionarios, etc).

# -------------------------- List Comprehensions ---------------------------
# Sintaxis: [expresion for elemento in iterable if condicion]

# --- Transformación simple ---
valores = [2, 5, 12, 10]
dobles = [x * 2 for x in valores]
print(f"Original: {valores} -> Dobles: {dobles}")

# --- Con condición de filtrado (if) ---
lista = [14, 5, 12, 16, 9, 7, 10]
solo_pares = [x for x in lista if x % 2 == 0]
print(f"\nSolo pares de {lista}: {solo_pares}")

# --- Múltiples condiciones `if` ---
pares_mayores_10 = [x for x in lista if x % 2 == 0 and x > 10]
print(f"Pares mayores que 10: {pares_mayores_10}")

# --- Condicional if-else (ternario) ---
# Sintaxis: [valor_si_true if condicion else valor_si_false for e in iterable]
pares_o_cero = [x if x % 2 == 0 else 0 for x in lista]
print(f"Pares o Cero (si es impar): {pares_o_cero}")

# --- Anidadas (ej. traspuesta de matriz) ---
matriz = [[1, 2, 3], [4, 5, 6]]
traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(f"\nMatriz: {matriz} -> Traspuesta: {traspuesta}")


# ----------------------- Dictionary Comprehensions ------------------------
# Sintaxis: {clave: valor for elemento in iterable if condicion}
dic_original = {"a": 1, "b": 2, "c": 3, "d": 4}
cuadrados_dic = {k: v**2 for k, v in dic_original.items() if v > 2}
print(f"\nDiccionario con valores > 2 al cuadrado: {cuadrados_dic}")


# -------------------------- Set Comprehensions ----------------------------
# Sintaxis: {expresion for elemento in iterable if condicion}
# Crea un conjunto (sin duplicados).
numeros_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_unicos_cuadrado = {x**2 for x in numeros_con_duplicados}
print(f"\nConjunto de cuadrados (únicos): {conjunto_unicos_cuadrado}")
