# ----------------------------------------
# ----- 2.1 TIPOS BÁSICOS Y VARIABLES -----
# ----------------------------------------

x = 5
x = "Hola"

# print(y) # NameError: name 'y' is not defined

x = 10
y = 3.5

print(int(y))
print(int("345"))

a = True

print(a)
print(bool(0))
print(bool(1))
print(bool(-5))

x = 5
print(type(x))

# -------------------------------------------
# ----- 2.2 OPERACIONES ARITMÉTICAS -----
# -------------------------------------------

# La guía de estilo recomienda:
# - Poner un espacio entre los operadores: `num = 10` (no `num=10`).
# - Nombres de variables en minúsculas: `unit_price` (no `unitPrice`).

# ------------------------------------
# ----- 2.3 ENTRADA/SALIDA (I/O) -----
# ------------------------------------

print("Mensaje sin variable")

x = 5

print("El valor es "+str(x))
print("El valor es ", x)

x = 5
a = x/3

print("El valor es {0} y si queremos otro valor sería así {1}".format(x, x/3))
print("El valor es {1} y si queremos otro valor sería así {0}".format(x, x/3))
print("El valor es {0} y si queremos otro valor sería así {a}".format(x, a=x/3))
print("El valor es {0:.3f} y si queremos otro valor sería así {a:.2f}".format(x, a=x/3))

print("\n--- Inicio de sección interactiva (input) ---")
a = int(input("Introduce el radio (int):"))
b = float(input("Introduce el radio (float):"))
a = b
a = "Ahora pasa a ser una cadena"

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
sum = num1 + num2

print("El resultado de sumar ",num1," y ",num2," es ",sum)
print("El resultado de sumar {0} y {1} es {2}".format(num1, num2, sum))
print("El resultado de sumar "+str(num1)+" y "+str(num2))
print("--- Fin de sección interactiva ---\n")


# -------------------
# ----- 2.4 MÓDULOS -----
# -------------------

import math

x = 10
print("La raíz cuadrada de", x, "es", math.sqrt(x))

# help(math)
# help(math.factorial)

from math import factorial
print(factorial(10))

from math import factorial as fac
print(fac(10))

from math import sin
from math import sin, cos
from math import *
