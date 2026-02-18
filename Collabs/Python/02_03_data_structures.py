# -------------------------
# ----- 4.1 LISTAS -----
# -------------------------

datos = []
datos = list()
datos = [4, "mensaje", -15, 3.4]

datos = [4, "mensaje", -15, 3.4]
print("Elemento de la pos 2:", datos[2])

datos[2] = 10
print(datos)

print("Penúltimo elemento:", datos[-2])

datos = [10, 11, 12, 13, 14]
print(type(datos))

print("Desde la posición 1 hasta una anterior a la 3:", datos[1:3])
print("Los dos primeros:", datos[:2])
print("Desde la posición 1 hasta el final:", datos[1:])
print("Desde la posición -1 hasta el final: ", datos[-1:])
print("Desde la posición 1 a la -2 (no incluida): ", datos[1:-2])
print("Desde la posición -4 a la -2 (no incluida): ", datos[-4:-2])
print("Aunque tenga un elemento, lo que devuelve la operación de slicing continúa siendo una lista:", type(datos[-1:]))
print("Si no especificamos índices, obtenemos todos los valores: ", datos[:])

print("Repetimos la lista dos veces:", datos * 2)
print("Creamos una lista con 5 ceros:", [0] * 5)

datos = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("Desde la posición 2 hasta la 7 (no incluida) pero de 3 en 3: ", datos[2:7:3])

datos = [4, "mensaje", -15, 3.4]

longitud = len(datos)
print(longitud)

datos.append(12)
print("Añado el 12 al final: ", datos)

datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

datos.extend([55, 22])
print("Combino dos listas: ", datos)

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

datos.remove(-15)
print("Elimino el -15: ",datos)

del(datos[2])
# res = datos.pop(2)
print("Elimino el de la pos 2: ",datos)

datos[:2] = []
print("Vacio desde la pos 0 hasta la 2: ",datos)

# datos = []
# datos.clear()
# del(datos)
print("La vacío entera: ",datos)

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

res = datos.count(-15)
print("Veces que aparece el -15: ",res)

res = datos.index(-15)
print("Posición del -15: ",res)

datos = ["esto", "es", "un", "mensaje"]
datos.sort()
print("Nuevos datos ordenados:", datos)
datos.sort(key=len)
print("Nuevos datos ordenados por longitud:", datos)

datos = [4, "mensaje", -15, 3.4]

for i in datos:
  print(i)

datos = [4, "mensaje", -15, 3.4]
is_34 = 3.4 in datos
print(is_34)
is_23 = 23 in datos
print(is_23)

lista = [5, 2, 3, 7, 4, 1, 7]
encontrado = False
i = 0
while (not encontrado) and (i < len(lista)):
  if lista[i] == 7:
    print("Encontrado en posición "+str(i))
    encontrado = True
  i += 1

if not encontrado:
  print("No se ha encontrado")

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    break
print("Fin")

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    continue
  print("Este código sólo se ejecuta si no entra por el if, ya que el continue se carga la iteración")
print("Fin")

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

random.shuffle(lista)
print(lista)

res = random.randint(1, 4)
print(res)

# -------------------------
# ----- 4.3 STRINGS -----
# -------------------------

palabra = "hola"

print(palabra[0])
print("Penúltimo caracter:", palabra[-2])
print(palabra[0:2])
print(palabra[:2])
print(palabra[-2:])

x = 485
print("El valor es "+str(x))

x = 485
print(type(x))
x = str(x)
print(type(x))

x = "esto es un mensaje"

print("upper:", x.upper())
print("title:", x.title())
print("replace:", x.replace("es","kk"))
print("format:", "La edad de {0} es {1}".format("Pepe", 25))
print("split:", x.split(" "))
print("partition:", x.partition("un"))

departure, separator, arrival = "Valencia:Londres".partition(":")
print("otro ejemplo: ",departure, separator, arrival)

for i in "Hola":
  print(i)
print("Fin")
