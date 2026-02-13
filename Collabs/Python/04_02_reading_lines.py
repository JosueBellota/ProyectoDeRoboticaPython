# 04_02_reading_lines.py

# Diferentes formas de leer un fichero línea a línea

# 1. Usando readline()
f = open("fichero.txt", "rt", encoding="utf-8")
linea1 = f.readline()
print(f"Línea 1: {linea1.strip()}") # strip() quita el 

f.close()

# 2. Recorriendo el objeto fichero (Forma más eficiente y recomendada)
print("Recorriendo con bucle for:")
f = open("fichero.txt", "rt", encoding="utf-8")
for linea in f:
    print(f"Leído: {linea.strip()}")
f.close()

# 3. Usando readlines() -> Devuelve una lista con todas las líneas
f = open("fichero.txt", "rt", encoding="utf-8")
lista_lineas = f.readlines()
print(f"Lista de líneas: {lista_lineas}")
f.close()

# 4. Escribir múltiples líneas con writelines()
f = open("fichero_lista.txt", "wt", encoding="utf-8")
lineas_a_escribir = ["Primera línea", "Segunda línea", "Tercera línea"]
f.writelines(lineas_a_escribir)
f.close()
