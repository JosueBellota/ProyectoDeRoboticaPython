################################################################################
#                                                                              #
#                         04_01_text_files.py                                  #
#                                                                              #
################################################################################

# --- Modos de apertura comunes ---
# 'r': Lectura (Read). Error si el fichero no existe.
# 'w': Escritura (Write). Sobrescribe el fichero si ya existe.
# 'a': Añadir (Append). Añade contenido al final del fichero.
# 't': Modo texto (por defecto).
# 'b': Modo binario.


# ---------------------- 1. Escritura en un fichero de texto ----------------------
# Usar 'with' asegura que el fichero se cierre automáticamente.
with open("fichero_ejemplo.txt", mode="w", encoding="utf-8") as f:
    f.write("Esto es un mensaje.\n")
    f.write("Y una nueva línea.\n")

print("Fichero 'fichero_ejemplo.txt' escrito.")


# ---------------------- 2. Lectura de un fichero de texto ----------------------
with open("fichero_ejemplo.txt", mode="r", encoding="utf-8") as f:
    # `read()` sin argumentos lee el fichero completo.
    contenido_completo = f.read()
    print("\nContenido completo del fichero:")
    print(contenido_completo)


# ---------------- 3. Posicionamiento manual: seek() y tell() ----------------
# `tell()`: Devuelve la posición actual del cursor (en bytes).
# `seek(n)`: Mueve el cursor a la posición `n` (en bytes).
with open("fichero_ejemplo.txt", mode="r", encoding="utf-8") as f:
    contenido_parcial = f.read(5)
    print(f"\nLeídos 5 caracteres: '{contenido_parcial}'")
    print(f"Posición actual del cursor: {f.tell()}")

    # Mover el cursor al inicio del fichero (posición 0).
    f.seek(0)
    print("Cursor movido al inicio (seek(0)).")
    
    contenido_desde_inicio = f.read(10)
    print(f"Leídos 10 caracteres desde el inicio: '{contenido_desde_inicio}'")
