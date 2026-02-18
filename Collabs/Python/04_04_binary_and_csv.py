################################################################################
#                                                                              #
#                      04_04_binary_and_csv.py                                 #
#                                                                              #
################################################################################

# Manejo de ficheros binarios y CSV.

# --------------------------- 1. Ficheros Binarios ---------------------------
# Para contenido no textual (imágenes, etc.). Se usa el modo 'b' ('rb', 'wb').
# Los datos se leen y escriben como `bytes`, no `str`. No se usa `encoding`.

# Ejemplo: Escribir y leer bytes.
datos_binarios = b'Hola Mundo Binario'
with open("fichero.bin", "wb") as f:
    f.write(datos_binarios)

with open("fichero.bin", "rb") as f:
    contenido_leido = f.read()
    print(f"Contenido binario leído: {contenido_leido}")
    print(f"Contenido decodificado: {contenido_leido.decode('utf-8')}")


# ---------------------------- 2. Ficheros CSV -----------------------------
# Para datos tabulares, usando el módulo `csv`.
import csv

datos_para_csv = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', '25', 'Madrid'],
    ['Maria', '30', 'Barcelona']
]

# --- Escritura de un fichero CSV ---
# `newline=''` evita saltos de línea extra en algunos SO.
with open('usuarios.csv', 'w', newline='', encoding='utf-8') as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerows(datos_para_csv)

print("\nFichero 'usuarios.csv' escrito.")

# --- Lectura de un fichero CSV ---
with open('usuarios.csv', 'r', encoding='utf-8') as file:
    lector_csv = csv.reader(file)
    
    print("Contenido leído del CSV:")
    for fila in lector_csv:
        print(f"  > {fila}")

# --- Nota sobre delimitadores ---
# Para usar, por ejemplo, punto y coma (;) en lugar de coma:
# lector_csv = csv.reader(file, delimiter=';')
