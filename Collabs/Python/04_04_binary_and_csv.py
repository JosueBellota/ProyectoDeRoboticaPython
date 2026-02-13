# 04_04_binary_and_csv.py
import csv

# --- 1. Ficheros Binarios (rb, wb) ---
# Se usan para imágenes, ejecutables, etc. No usan 'encoding'.
try:
    with open('lena.png', 'rb') as f:
        contenido = f.read(20) # Leemos los primeros 20 bytes
        print(f"Primeros bytes binarios: {contenido}")
except FileNotFoundError:
    print("Nota: No se encontró 'lena.png' para el ejemplo binario.")


# --- 2. Ficheros CSV ---
# Útiles para datos tabulares.

# Crear un CSV de ejemplo
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', '25', 'Madrid'],
    ['Maria', '30', 'Barcelona'],
    ['Pedro', '22', 'Valencia']
]

with open('usuarios.csv', 'wt', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(datos)

# Leer un CSV
print("Contenido del CSV:")
with open('usuarios.csv', 'rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    for fila in reader:
        print(f"Fila: {fila}")

# Nota sobre delimitadores:
# Si el CSV usa ';' o tabs, se especifica: csv.reader(file, delimiter=';')
