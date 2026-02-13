# 03_04_tuples.py

# Las tuplas son secuencias INMUTABLES (no se pueden modificar tras su creación)

# Creación
tupla1 = (25, 12, 14, 29)
tupla2 = 25, 12, 14, 29 # Paréntesis opcionales
print(f"Tupla 1: {tupla1}")

# Tupla de un solo elemento (requiere coma final)
tupla_unica = (43,)
print(f"Tupla única: {tupla_unica} - Tipo: {type(tupla_unica)}")

# Acceso (igual que las listas, por índice)
print(f"Primer elemento: {tupla1[0]}")

# Métodos disponibles (solo de lectura)
print(f"Longitud: {len(tupla1)}")
print(f"Contar apariciones de 12: {tupla1.count(12)}")
print(f"Índice del valor 14: {tupla1.index(14)}")

# Intentar modificar una tupla daría error:
# tupla1[0] = 10 # TypeError: 'tuple' object does not support item assignment

# Uso común: Retornar varios valores en una función
def area_y_perimetro(base, altura):
    area = base * altura
    perimetro = (base * 2) + (altura * 2)
    return area, perimetro # Se devuelve como una tupla

b, a = 2, 3
res_area, res_perim = area_y_perimetro(b, a) # Unpacking de la tupla
print(f"
Rectángulo {b}x{a}: Área={res_area}, Perímetro={res_perim}")
