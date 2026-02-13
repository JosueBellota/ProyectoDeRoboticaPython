# 03_03_comprehensions.py

# Comprehensions: forma elegante de crear colecciones

valores = [2, 5, 12, 10]

# --- List Comprehension ---
# [expresión for elemento in iterable if condición]

# 1. Transformación simple
dobles = [x * 2 for x in valores]
print(f"Original: {valores} -> Dobles: {dobles}")

# 2. Con filtrado (if)
lista = [14, 5, 12, 16, 9, 7, 10]
solo_pares = [x for x in lista if x % 2 == 0]
print(f"Solo pares de {lista}: {solo_pares}")

# 3. Múltiples condiciones
pares_mayores_10 = [x for x in lista if x % 2 == 0 if x > 10]
print(f"Pares > 10: {pares_mayores_10}")

# 4. If-Else (cambia la posición)
# [valor_if if condicion else valor_else for elemento in iterable]
pares_o_cero = [x if x % 2 == 0 else 0 for x in lista]
print(f"Pares o cero: {pares_o_cero}")

# 5. Anidadas (ej. Traspuesta de matriz)
matriz = [[1, 2, 3, 4], [4, 5, 6, 8]]
traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(f"Matriz: {matriz}")
print(f"Traspuesta: {traspuesta}")


# --- Dictionary Comprehension ---
# {clave: valor for elemento in iterable if condición}

dic_original = {"a": 1, "b": 2, "c": 3, "d": 4}
cuadrados_dic = {k: v**2 for k, v in dic_original.items() if v > 2}
print(f"
Diccionario original: {dic_original}")
print(f"Diccionario filtrado y al cuadrado (v > 2): {cuadrados_dic}")
