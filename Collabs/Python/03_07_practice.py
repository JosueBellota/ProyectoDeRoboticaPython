################################################################################
#                                                                              #
#                       03_07_practice.py (Solutions)                          #
#                                                                              #
################################################################################

# --- 1. Eliminar la primera letra de una lista de palabras ---
def without_first_letter(palabras):
    return [palabra[1:] for palabra in palabras]

# Prueba
lista_palabras = ["Hola", "Python", "Mundo"]
print(f"1. Sin primera letra: {without_first_letter(lista_palabras)}")


# --- 2. Encontrar el valor mínimo en una lista ---
def get_minimum(numeros):
    return min(numeros) if numeros else None

# Prueba
lista_numeros_1 = [4, 1, 9, -3, 8]
print(f"\n2. Mínimo de {lista_numeros_1}: {get_minimum(lista_numeros_1)}")


# --- 3. Cuadrados de números mayores que 10 ---
def squares_greater_than_10(numeros):
    return [n**2 for n in numeros if n > 10]

# Prueba
lista_numeros_2 = [5, 12, 8, 15, 10]
print(f"\n3. Cuadrados de >10 en {lista_numeros_2}: {squares_greater_than_10(lista_numeros_2)}")


# --- 4. Filtrar un diccionario por valor (precio > 2.0) ---
frutas = {"Manzana": 1.5, "Banana": 0.8, "Kiwi": 3.0, "Mango": 2.5}
frutas_caras = {fruta: precio for fruta, precio in frutas.items() if precio > 2.0}

# Prueba
print("\n4. Frutas caras (> 2.0€):", frutas_caras)


# --- 5. Generador de cuenta atrás ---
def cuenta_atras(numero_inicial):
    while numero_inicial >= 0:
        yield numero_inicial
        numero_inicial -= 1

# Prueba
print("\n5. Cuenta atrás desde 5:")
for numero in cuenta_atras(5):
    print(numero, end=" ")
print()
