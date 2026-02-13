# 04_03_with_context.py

# El bloque 'with' asegura que el fichero se cierre automáticamente,
# incluso si ocurre un error durante el procesamiento.
# Es la forma profesional de manejar ficheros en Python.

nombre_fichero = "fichero.txt"

# Escritura con 'with'
with open(nombre_fichero, "wt", encoding="utf-8") as f:
    f.write("Línea 1 con context manager")
    f.write("Línea 2 con context manager")

# Lectura con 'with'
print(f"Leyendo '{nombre_fichero}':")
with open(nombre_fichero, "rt", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# Aquí el fichero ya está cerrado automáticamente
# No hace falta llamar a f.close()
