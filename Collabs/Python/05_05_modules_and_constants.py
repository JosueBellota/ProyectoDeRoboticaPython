# 05_05_modules_and_constants.py

# 2 Módulos y paquetes

# Opción 1 para importar un módulo completo
# import my_module # Suponiendo que my_module.py existe
# my_module.some_function()

# Opción 2 para importar elementos específicos de un módulo
# from my_module import MyClass, my_function
# MyClass()
# my_function()

# from my_module import * # Importa todo, no recomendado en producción

# if __name__ == "__main__":
# Este bloque se ejecuta solo cuando el script es ejecutado directamente,
# no cuando es importado como un módulo.
#   print("Este código se ejecuta solo cuando 05_05_modules_and_constants.py es el script principal.")

# 2.1 Constantes

# Definición de una constante (por convención, en MAYÚSCULAS)
PI = 3.14159

# Para usar esta constante en otro archivo:
# import 05_05_modules_and_constants as constants_file
# print(constants_file.PI)

# O
# from 05_05_modules_and_constants import PI
# print(PI)


# Agrupando constantes dentro de una clase
class States:
    INIT = 0
    ACTIVE = 1
    IDDLE = 2
    STOP = 3

# Para usar estas constantes:
# print(States.ACTIVE)

# O desde otro archivo:
# from 05_05_modules_and_constants import States
# print(States.STOP)
