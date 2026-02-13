# 04_01_text_files.py

# Para trabajar con ficheros usamos open(file, mode, encoding)
# Modos comunes: 
# 'r' - lectura (por defecto)
# 'w' - escritura (sobreescribe)
# 'a' - añadir (append)
# 't' - modo texto (por defecto)
# 'b' - modo binario

# --- 1. Escritura básica ---
# 'wt' -> write text
f = open("fichero.txt", mode="wt", encoding="utf-8")
f.write("Esto es un mensaje.")
f.write("Esto es otro mensaje en la misma línea. ")
f.write("Y una nueva línea.")
f.close() # ¡Importante cerrar siempre!

# --- 2. Lectura básica ---
# 'rt' -> read text
f = open("fichero.txt", mode="rt", encoding="utf-8")

# Leer un número específico de caracteres
diez_caracteres = f.read(10)
print(f"Primeros 10 caracteres: '{diez_caracteres}'")

# Leer el resto del fichero
resto = f.read()
print(f"Resto del fichero:{resto}")
f.close()

# --- 3. Posicionamiento: seek() y tell() ---
f = open("fichero.txt", mode="rt", encoding="utf-8")
f.read(5)
print(f"Posición actual tras leer 5 chars: {f.tell()}")

f.seek(0) # Volver al inicio
print(f"Volvemos a leer desde el inicio: {f.read(10)}")
f.close()
