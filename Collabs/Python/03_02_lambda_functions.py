# 03_02_lambda_functions.py

# Las funciones lambda son funciones anónimas de una sola línea
# Sintaxis: lambda parámetros : expresión

# Ejemplo simple: multiplicación
multiplicar = lambda x, y : x * y
print(f"Resultado lambda (5 * 2): {multiplicar(5, 2)}")

# Es equivalente a:
def multiplica_tradicional(x, y):
    return x * y

# Uso con funciones de orden superior (como sorted, filter, map)
palabras = ["Python", "es", "genial", "y", "potente"]
# Ordenar por la longitud de la palabra usando lambda
palabras_ordenadas = sorted(palabras, key=lambda p: len(p))
print(f"Palabras ordenadas por longitud: {palabras_ordenadas}")

# Ejemplo de filtrado (números pares)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")
