################################################################################
#                                                                              #
#                      03_02_lambda_functions.py                               #
#                                                                              #
################################################################################

# Las funciones lambda son funciones anónimas de una sola línea.
# Sintaxis: lambda parámetros: expresión

# ---------------------- Ejemplo simple de función lambda ----------------------
multiplicar = lambda x, y: x * y
resultado = multiplicar(5, 2)
print(f"Resultado de la lambda (5 * 2): {resultado}")


# ----- Uso de lambdas con funciones de orden superior (sorted, filter, map) ----

# --- Con sorted() ---
# 'key' especifica una función que se llama para cada elemento antes de comparar.
palabras = ["Python", "es", "genial", "y", "muy", "potente"]
palabras_ordenadas = sorted(palabras, key=lambda palabra: len(palabra))
print("\nPalabras ordenadas por longitud:", palabras_ordenadas)

# --- Con filter() ---
# Crea una lista con los elementos para los que la función devuelve True.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("\nNúmeros pares filtrados:", numeros_pares)


# --- Con map() ---
# Aplica una función a cada elemento de un iterable.
numeros_al_cuadrado = list(map(lambda x: x ** 2, numeros))
print("\nNúmeros al cuadrado:", numeros_al_cuadrado)
