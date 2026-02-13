# 03_06_iterators_generators.py

# --- Iteradores ---
# Un iterable (lista, string, dic) puede convertirse en iterador con iter()
lista = [10, 20, 30]
it = iter(lista)

print("Usando next():")
print(next(it)) # 10
print(next(it)) # 20
# print(next(it)) # 30
# next(it) # Lanzaría StopIteration al agotarse


# --- Generadores ---
# Funciones que usan 'yield' para devolver valores uno a uno, manteniendo el estado

def generador_pares(limite):
    """Genera números pares hasta un límite"""
    n = 0
    while n <= limite:
        yield n # La función se "pausa" aquí y devuelve el valor
        n += 2

print("
Recorriendo un generador con un bucle for:")
for p in generador_pares(10):
    print(p, end=" ")
print()

# Generador infinito (ejemplo conceptual)
def fibonacci():
    """Generador infinito de la serie de Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("
Primeros 5 números de Fibonacci:")
fib = fibonacci()
for _ in range(5):
    print(next(fib), end=" ")
print()

# Ventaja: Los generadores son eficientes en memoria porque no guardan 
# toda la lista, solo calculan el siguiente valor bajo demanda.
