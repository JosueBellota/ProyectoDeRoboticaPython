################################################################################
#                                                                              #
#                   03_06_iterators_generators.py                              #
#                                                                              #
################################################################################

# Mecanismos para manejar secuencias de datos de forma eficiente en memoria.

# -------------------------------- Iteradores --------------------------------
# Un iterador es un objeto que representa un flujo de datos.
# Se obtiene de un iterable (lista, tupla...) con `iter()`.
# Se consume con `next()`.
print("--- Iterador ---")
lista_iterable = [10, 20, 30]
mi_iterador = iter(lista_iterable)

# `next()` devuelve el siguiente elemento o lanza StopIteration si se agota.
print("Elemento 1:", next(mi_iterador))
print("Elemento 2:", next(mi_iterador))

# El bucle `for` usa iteradores internamente de forma automática.


# ------------------------------- Generadores --------------------------------
# Son una forma sencilla de crear iteradores usando funciones con la palabra `yield`.
# `yield` "pausa" la función y devuelve un valor, guardando el estado para la próxima llamada.

# --- Generador finito: números pares ---
def generador_pares(limite):
    numero = 0
    while numero <= limite:
        yield numero
        numero += 2

print("\n--- Generador de Pares ---")
# El generador se consume al iterar sobre él.
for p in generador_pares(10):
    print(p, end=" ")
print()


# --- Generador infinito: serie de Fibonacci ---
# Ideales para secuencias infinitas, pues solo calculan el valor cuando se pide.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n--- Generador Infinito (Fibonacci) ---")
generador_fib = fibonacci()
print("Primeros 10 números de Fibonacci:")
for _ in range(10):
    print(next(generador_fib), end=" ")
print()

# Ventaja principal: Eficiencia de memoria. No se guarda la secuencia completa.
