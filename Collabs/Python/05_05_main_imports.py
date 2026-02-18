################################################################################
#                                                                              #
#                      05_05_main_imports.py                                   #
#                                                                              #
################################################################################

# Un "módulo" es simplemente un fichero .py que contiene código de Python.
# Podemos importar ese código para usarlo en otros ficheros.

# --- 1. Importar el módulo completo ---
# Se importa el fichero entero y se necesita usar el nombre del módulo como prefijo.
print("--- 1. Importando 'mi_modulo' ---")
import mi_modulo

# Para usar la función y la clase, debemos usar `mi_modulo.`
mi_modulo.saludar_modulo("Ana")
calculadora_1 = mi_modulo.Calculadora()
print(f"Resultado: {calculadora_1.sumar(10, 5)}")


# --- 2. Importar elementos específicos con `from` ---
# Se importan solo las partes deseadas del módulo. Se pueden usar sin prefijo.
print("\n--- 2. Importando con 'from' ---")
from mi_modulo import saludar_modulo, VERSION

# Ya no es necesario el prefijo `mi_modulo.`
saludar_modulo("Juan")
print(f"La versión del módulo importado es: {VERSION}")


# --- 3. Importar con un alias ---
# Se le da un "apodo" o alias a un módulo importado. Es muy útil para
# nombres largos o para evitar colisiones de nombres.
print("\n--- 3. Importando con un alias ---")
import mi_modulo as modulo_custom

modulo_custom.saludar_modulo("Pedro")
calc_custom = modulo_custom.Calculadora()
print(f"Suma con alias: {calc_custom.sumar(100, 200)}")


# --- 4. Importar constantes ---
# Es una práctica común tener un fichero solo para constantes.
print("\n--- 4. Importando constantes ---")
from constantes import PI, EstadoUsuario

print(f"El valor de PI es {PI}")
print(f"Un estado posible para un usuario es: {EstadoUsuario.ACTIVO}")


# --- 5. El bloque `if __name__ == "__main__"` ---
# Cuando importamos `mi_modulo`, el código dentro de su bloque `if __name__ == "__main__"`
# NO se ejecutó. Esto es crucial para que los módulos no ejecuten código de prueba
# al ser importados.
#
# `__name__` es una variable especial que Python crea en cada fichero:
# - Si el fichero es el punto de entrada (el que ejecutas), `__name__` vale "__main__".
# - Si el fichero es importado, `__name__` vale el nombre del fichero (ej. "mi_modulo").

print("\n--- 5. Comprobando __name__ ---")
print(f"El valor de `__name__` en este fichero es: '{__name__}'")
