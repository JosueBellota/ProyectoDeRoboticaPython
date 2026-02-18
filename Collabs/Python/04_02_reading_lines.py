################################################################################
#                                                                              #
#                      04_02_reading_lines.py                                  #
#                                                                              #
################################################################################

# Formas de leer y escribir un fichero de texto línea por línea.

# Fichero de ejemplo para las pruebas.
lineas_para_el_fichero = [
    "Esta es la primera línea.\n",
    "Aquí va la segunda.\n",
    "Y finalmente, la tercera línea.\n"
]
with open("fichero_para_lineas.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas_para_el_fichero)


# ---------------------- 1. Leer línea a línea con `readline()` ----------------------
# Lee una sola línea, incluyendo el salto de línea `\n`.
with open("fichero_para_lineas.txt", "r", encoding="utf-8") as f:
    linea1 = f.readline().strip() # .strip() quita el '\n' y espacios
    linea2 = f.readline().strip()
    print(f"Línea 1: '{linea1}'")
    print(f"Línea 2: '{linea2}'")


# ------------ 2. Iterar sobre el objeto fichero (Forma recomendada) ------------
# La forma más eficiente y común para leer línea a línea.
print("\n--- Iterando sobre el fichero ---")
with open("fichero_para_lineas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(f"  > {linea.strip()}")


# ---------------- 3. Leer todas las líneas con `readlines()` ----------------
# Lee el fichero completo y devuelve una LISTA de líneas.
# Puede consumir mucha memoria en ficheros grandes.
with open("fichero_para_lineas.txt", "r", encoding="utf-8") as f:
    lista_de_lineas = f.readlines()

print("\nResultado de readlines() (es una lista):")
print(lista_de_lineas)


# ----------------- 4. Escribir líneas desde una lista con `writelines()` -----------------
# Escribe un iterable de strings. No añade saltos de línea (`\n`) automáticamente.
lineas_a_escribir = ["Inicio del nuevo fichero.\n", "Continuación.\n", "Fin."]
with open("fichero_escrito_con_writelines.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas_a_escribir)

print("\n'fichero_escrito_con_writelines.txt' creado.")
