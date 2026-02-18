################################################################################
#                                                                              #
#              04_03_with_context (Context Managers)                           #
#                                                                              #
################################################################################

# El manejador de contexto `with` es la forma recomendada para trabajar con ficheros.
#
# Ventajas:
# 1. Cierre automático: El fichero se cierra al salir del bloque `with`.
# 2. Seguridad ante excepciones: El fichero se cierra incluso si ocurre un error.

nombre_fichero = "fichero_con_with.txt"

# ------------------- Escritura con `with` -------------------
print("--- Escribiendo con `with` ---")
try:
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        f.write("Línea 1 escrita con el context manager.\n")
        f.write("Línea 2, también con 'with'.\n")
        # Si un error ocurriese aquí, el fichero se cerraría igual.

    # Al salir del bloque, el fichero ya está cerrado.
    print(f"El fichero '{nombre_fichero}' se ha cerrado automáticamente.")

except IOError as e:
    print(f"Ocurrió un error de escritura: {e}")


# -------------------- Lectura con `with` --------------------
print(f"\n--- Leyendo con `with` ---")
try:
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        # El fichero 'f' está abierto solo dentro de este bloque.
        for linea in f:
            print(f"  > {linea.strip()}")

except FileNotFoundError:
    print(f"Error: El fichero '{nombre_fichero}' no existe.")

# No es necesario llamar a f.close().
