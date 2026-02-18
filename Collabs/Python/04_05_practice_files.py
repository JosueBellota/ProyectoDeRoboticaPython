################################################################################
#                                                                              #
#                04_05_practice_files.py (Solutions)                           #
#                                                                              #
################################################################################

# --- 1. Generar un fichero con números y sus cuadrados ---
def generar_cuadrados():
    with open("cuadrados.txt", "w", encoding="utf-8") as f:
        for i in range(1, 11):
            f.write(f"{i} al cuadrado es {i*i}\n")
    print("1. Fichero 'cuadrados.txt' generado.")


# Prueba
generar_cuadrados()


# --- 2. Encontrar la palabra más larga en un fichero ---
with open("palabras.txt", "w", encoding="utf-8") as f:
    f.write("python\nprogramacion\nelectroencefalografista\n")

def palabra_mas_larga(nombre_fichero):
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            palabras = [line.strip() for line in f]
            return max(palabras, key=len)
    except (FileNotFoundError, ValueError): # ValueError si el fichero está vacío
        return None

# Prueba
fichero_palabras = "palabras.txt"
palabra = palabra_mas_larga(fichero_palabras)
print(f"\n2. Palabra más larga en '{fichero_palabras}': {palabra}")


# --- 3. Filtrar palabras que contienen una letra específica ---
def filtrar_por_letra(nombre_fichero, letra):
    print(f"\n3. Palabras en '{nombre_fichero}' con la letra '{letra}':")
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            for palabra in f:
                if letra in palabra:
                    print(f"  - {palabra.strip()}")
    except FileNotFoundError:
        print(f"  Error: Fichero '{nombre_fichero}' no encontrado.")

# Prueba
filtrar_por_letra("palabras.txt", "g")


# --- 4. Anonimizar un fichero reemplazando un nombre ---
with open("interview.txt", "w", encoding="utf-8") as f:
    f.write("En la última reunión, Trump expuso sus ideas. El Sr. Trump es polémico.\n")

def anonimizar_fichero(f_in, f_out, texto_a_cambiar, reemplazo):
    try:
        with open(f_in, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        contenido_anonimo = contenido.replace(texto_a_cambiar, reemplazo)
        
        with open(f_out, "w", encoding="utf-8") as f:
            f.write(contenido_anonimo)
        
        print(f"\n4. Fichero '{f_in}' anonimizado como '{f_out}'.")
    except FileNotFoundError:
        print(f"  Error: Fichero de entrada '{f_in}' no existe.")

# Prueba
anonimizar_fichero("interview.txt", "anonymous.txt", "Trump", "Mr. X")
