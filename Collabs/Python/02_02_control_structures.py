# ---------------------------------
# ----- 3.1 IF Y ELSE -----
# ---------------------------------

num = 7

if num >= 5:
  print("El número es mayor o igual a 5")
else:
  print("El número es menor que 5")

print("Esta línea se ejecuta siempre")


color = "azul"

if color == "rojo":
  print("El color es rojo")
else:
  if color == "azul":
    print("El color es azul")
  else:
    print("El color no es ni rojo ni azul")

print("Esta línea se ejecuta siempre")

color = "rojo"

if color == "rojo":
  print("El color es rojo")
elif color == "azul":
  print("El color es azul")
else:
  print("El color no es ni rojo ni azul")

print("Esta línea se ejecuta siempre")


# ---------------------------------
# ----- 3.2 OPERACIONES LÓGICAS -----
# ---------------------------------

a = True
b = False
x = 7
y = 0
print(a < b)
print(x >= y)
print(not a)
print(not y)
print(a and b)
print(a or b)


x = 6
y = 2

if x % 2 == 0 and (not ( x > 5 )):
  print("entro por if")
else:
  print("entro por else")


# ---------------------------------
# ----- 3.4 WHILE Y FOR -----
# ---------------------------------

i = 0

while i < 5:
  print(i)
  i+=1


for i in range(10):
  print(i)

print("Fin")


for i in range(1,10):
  print(i)

print("Fin")


for i in 1, 2, 3, "casa", "coche", 3.14:
  print(i)

print("Fin")
