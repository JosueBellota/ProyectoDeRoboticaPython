# 04_05_practice_files.py

# EJERCICIOS DE FICHEROS

# 1. Programa que genere un fichero 'cuadrados.txt' con los números del 1 al 10 y sus cuadrados.
def generar_cuadrados():
    pass

# 2. Función que reciba el nombre de un fichero con palabras (una por línea) 
# y devuelva la palabra más larga y su longitud.
def palabra_mas_larga(nombre_fichero):
    pass

# 3. Función que recibe nombre de fichero y una letra, y muestra las palabras 
# que contienen esa letra.
def filtrar_por_letra(nombre_fichero, letra):
    pass

# 4. Función que anonimice un fichero. Cambiar "Trump" por "Mr. X".
# Lee de 'interview.txt' y escribe en 'anonymous.txt'.
def anonimizar_fichero(entrada, salida):
    # Tip: usar el método replace() de los strings
    pass

# --- ESPACIO PARA PRUEBAS ---
if __name__ == "__main__":
    # Puedes crear un fichero de prueba rápido:
    with open("test_palabras.txt", "w") as f:
        f.write("python programacion ejercicio diccionario")
    
    print("Ficheros de prueba creados.")
