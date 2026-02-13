# 02_03_data_structures.py
# Apuntes generados a partir de 02_Introducción_a_Python.ipynb
# -----------------------------------------------------------

# # 4 Estructuras de datos

# En Python existen diversas estructuras de datos muy usadas. A continuación comentaremos las listas y los strings, trabajando con todo lo aprendido hasta ahora.

# ## 4.1 Listas

# Las listas son secuencias de elementos separados por comas. Dentro de una lista, cada dato ocupa una posición (primero, segundo, tercero, etc.). La lista es una estructura que puede crecer o decrecer de forma **dinámica** según añadamos o eliminemos datos.
# 
# El acceso a cada valor se realiza por su posición de forma similar a otros lenguajes de programación.
# 
# A diferencia de otros lenguajes, en Python, las listas **pueden contener cualquier tipo de valor** incluso otras colecciones de datos.
# 
# A continuación puedes ver algunas de las operaciones más habituales sobre listas:

#Creamos una lista:
datos = [] #vacía
datos = list() #otra forma
datos = [4, "mensaje", -15, 3.4] #con elementos

# Dos de las operaciones más comunes que podemos utilizar con listas son **indexing** y **slicing**. La operación de **indexing** nos permite acceder a **un elemento** de la lista a través de su posición (índice):

datos = [4, "mensaje", -15, 3.4]
print("Elemento de la pos 2:", datos[2])

#Modificamos un valor de la lista
datos[2] = 10
print(datos)

# También podemos utilizar **índices negativos**, donde el índice -1 hace referencia al último número de la lista:
# 
# <figure style="text-align:center">
#   <center>
#   <img width = "30%" src="https://s3imagenes.s3-us-west-2.amazonaws.com/index_array.png"/>
#   <figcaption align="center">Índices de una lista</figcaption>
#   </center>
# </figure>

#Índices negativos (del final hacia adelante, siendo -1 el último)
print("Penúltimo elemento:", datos[-2])

# Si lo que queremos es acceder a un **conjunto de elementos** de una lista, entonces debemos utilizar **slicing**. Este tipo de operaciones nos permite trocear una lista. Por ejemplo, a continuación puedes ver varios ejemplos donde troceamos una lista. Ten en cuenta que lo que te devuelve este tipo de operaciones también es de tipo **lista**:

datos = [10, 11, 12, 13, 14]
print(type(datos))

#Slicing para obtener una porción de la lista
print("Desde la posición 1 hasta una anterior a la 3:", datos[1:3])
print("Los dos primeros:", datos[:2])
print("Desde la posición 1 hasta el final:", datos[1:])
print("Desde la posición -1 hasta el final: ", datos[-1:])
print("Desde la posición 1 a la -2 (no incluida): ", datos[1:-2])
print("Desde la posición -4 a la -2 (no incluida): ", datos[-4:-2])
print("Aunque tenga un elemento, lo que devuelve la operación de slicing continúa siendo una lista:", type(datos[-1:]))
print("Si no especificamos índices, obtenemos todos los valores: ", datos[:])

# También podemos realizar otro tipo de operaciones con listas:

#Repetir elementos
print("Repetimos la lista dos veces:", datos * 2)
print("Creamos una lista con 5 ceros:", [0] * 5)

# También podemos utilizar **steps** para saltarnos algunos elementos en la operación de slicing. En el siguiente ejemplo, el valor 3 indica que nos saltaremos 3 elementos después de cada selección. Si no le pasamos steps, se considera 1:

datos = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("Desde la posición 2 hasta la 7 (no incluida) pero de 3 en 3: ", datos[2:7:3])

# ¿Y si hacemos `datos[:7:3]`? pues devolvería desde el principio hasta la posición 7 (no incluida) pero de 3 en 3.

# Las listas nos ofrecen varios métodos muy útiles para trabajar con ellas, entre los que destacamos los siguientes:
# * `len()` Devuelve la longitud de la lista.
# * `append()` Añade un elemento al final de la lista.
# * `clear()` Elimina todos los elementos de la lista, dejándola vacía.
# * `copy()` Crea una copia de la lista.
# * `count()` Cuenta cuántas veces aparece un elemento en la lista.
# * `extend()` Añade los elementos de una lista al final de otra.
# * `index()` Devuelve la posición de un elemento dentro de la lista.
# * `insert()` Añade un elemento en una determinada posición de la lista.
# * `pop()` Elimina un elemento de la lista y lo devuelve.
# * `del()` Elimina un elemento de la lista por su posición.
# * `remove()` Elimina un elemento de la lista por su valor.
# * `reverse()` Invierte el orden de elementos de una lista.
# * `sort()` Ordena una lista. Con el parámetro reverse=True especificamos que sea orden inverso.
# 
# En el siguiente enlace puedes encontrar todas las funciones: https://python-reference.readthedocs.io/en/latest/docs/list/

datos = [4, "mensaje", -15, 3.4]

#Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

#Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

#Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

#Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

#Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

#Eliminar un elemento (si hay varios, el primero que encuentra)
datos.remove(-15)
print("Elimino el -15: ",datos)

#Eliminar el elemento de determinada posición
del(datos[2])
#Otra forma mediante la que nos podemos guardar el valor eliminado
#res = datos.pop(2)
print("Elimino el de la pos 2: ",datos)

#Vaciar parcialmente una lista
datos[:2] = []
print("Vacio desde la pos 0 hasta la 2: ",datos)

#Vaciarla totalmente
#datos = []
#Otra forma
#datos.clear()
#Otra forma que borra incluso la lista
#del(datos)
print("La vacío entera: ",datos)

datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

#Contar cuántas veces aparece un elemento en la lista
res = datos.count(-15)
print("Veces que aparece el -15: ",res)

#Encontar el índice de un elemento de la lista (su primera aparición)
res = datos.index(-15)
print("Posición del -15: ",res)

#Ordenar de varias formas. Observa como podemos ordenar por longitud:
datos = ["esto", "es", "un", "mensaje"]
datos.sort()
print("Nuevos datos ordenados:", datos)
datos.sort(key=len)
print("Nuevos datos ordenados por longitud:", datos)

#Invertir: datos.reverse()
#Copiar: copia = datos.copy()

# Para recorrer una lista podemos utilizar un bucle ```for```:

datos = [4, "mensaje", -15, 3.4]

for i in datos:
  print(i)

# Para comprobar si un item está en una lista, podemos hacer el típico bucle que recorra todos los elementos, pero también podemos utilizar la instrucción ```in``` que es más cómoda. Observa el siguiente ejemplo y cómo lo tendríamos que hacer de una manera más manual:

#Ejemplo con in
datos = [4, "mensaje", -15, 3.4]

is_34 = 3.4 in datos
print(is_34)

is_23 = 23 in datos
print(is_23)

#Ejemplo manual
lista = [5, 2, 3, 7, 4, 1, 7]
encontrado = False
i = 0

while (not encontrado) and (i < len(lista)): #Los paréntesis son para facilitar la lectura, pero no son necesarios
  if lista[i] == 7:
    print("Encontrado en posición "+str(i))
    encontrado = True
  i += 1 #No existe la instrucción i++

if not encontrado:
  print("No se ha encontrado")

# Aunque algunos puristas están en contra de utilizarla, la instrucción ```break``` nos permite romper un bucle en un determinado momento:

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    break

print("Fin")

# Y por supuesto, también podemos utilizar la instrucción ```continue``` para romer una iteración determinada:

for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    continue
  print("Este código sólo se ejecuta si no entra por el if, ya que el continue se carga la iteración")

print("Fin")

# El **módulo random** nos permite realizar acciones aleatorias como generar números aleatorios, imprimir un valor de una lista, etc.

import random

#imprimimos un valor aleatorio
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

#barajamos una lista
random.shuffle(lista)
print(lista)

#creamos un entero aleatorio entre 1 y 4 (ambos incluidos)
res = random.randint(1, 4)
print(res)

# ## 4.2 Ejercicios

# Puedes intentar hacer algunos de estos ejercicios para practicar con listas:
# 
# 1. Dada una lista de enteros, muestra por pantalla si un número introducido por teclado está en la primera o en la última posición. La longitud mínima de la lista será de 1, en caso contrario, el programa terminará.
# 
# 2. Pide 4 números y añádelos a una lista. Después, rota los elementos y guárdalos en una nueva lista (el último es el primero, etc.), mostrando por pantalla esta nueva lista.
# 
# 3. Dadas dos listas de longitudes diferentes, averiguar si el primero o el último elemento de ambas listas es el mismo. En este caso, eliminar dicho elemento y mostrar las listas resultantes.
# 
# 4. Dada una lista de enteros, averiguar si el primer o el último elemento es el mayor y sustituir el resto de elementos por éste (sin contar el primero el último). Por ejemplo, la lista [11, 5, 9, 7] debería quedar como [11, 11, 11, 7].
# 
# 5. Calcular la cantidad de números impares que hay en una lista de enteros.
# 
# 6. Dada una lista de enteros, mostrar por pantalla la diferencia entre el mayor y el menor valor de la lista. Prueba a utilizar funciones del API para obtener estos valores.
# 
# 7. Dada una lista de enteros, devolver la media de todos los valores. Prueba a buscar en el API.
# 
# 8. Dada una lista de enteros, mostrar por pantalla si hay algún número que esté repetido en dos posiciones consecutivas.
# 
# 9. Dada una lista de enteros, elegir un número aleatorio de la lista.

# ## 4.3 Strings

# Los strings en Python son una estructura de datos similar a otros lenguajes. Podemos verlos como una cadena de caracteres:

palabra = "hola"

#Mostramos el primer caracter
print(palabra[0])

#Índices negativos (del final hacia adelante, siendo -1 el último)
print("Penúltimo caracter:", palabra[-2])

#Slicing: mostramos los dos primeros caracteres
print(palabra[0:2])
print(palabra[:2])

#Los dos últimos
print(palabra[-2:])

# Anteriormente, también hemos visto cómo hacer un casting de una variable de otro tipo (p.e. int) para poderla concatenar con otro string:

x = 485
print("El valor es "+str(x))

# Aprovechemos para recordar la función ```type()```, que nos devuelve el tipo de una variable:

x = 485
print(type(x))

x = str(x)
print(type(x))

# Con la función ```help(str)``` podemos ver los métodos de la clase ```str```, algunas de las cuáles son las siguientes:
# *   ```lower()```: transforma a minúsculas la cadena pasada como parámetro
# *   ```upper()```: transforma a mayúsculas la cadena pasada como parámetro
# *   ```title()```: transforma a mayúscula el carácter inicial de cada palabra
# *   ```replace()```: busca el patrón (arg2) en arg1 y los substituye por el valor del arg3. Ejemplo: ```arg1.replace(arg2,arg3)```
# *   ```format()```: reemplaza cada uno de sus argumentos por las marcas ```{i}``` incluidas en la cadena.
# *   ```len()``` devuelve la longitud de la que cadena pasada por parámetro
# *   ```split()```: separa un string por el delimitador que se pasa como parámetro.
# *   ```partition()```: separa un string en tres partes (antes del separador, el separador mismo y después del separador).
# 
# En el siguiente enlace tienes puedes encontrar más funciones: https://python-reference.readthedocs.io/en/latest/docs/str/

x = "esto es un mensaje"

print("upper:", x.upper())
print("title:", x.title())
print("replace:", x.replace("es","kk"))
print("format:", "La edad de {0} es {1}".format("Pepe", 25))
print("split:", x.split(" "))
print("partition:", x.partition("un")) #devuelve una lista, esto lo veremos más adelante

departure, separator, arrival = "Valencia:Londres".partition(":")
print("otro ejemplo: ",departure, separator, arrival)

# También podemos iterar por los caracteres de un string con la instrucción `for`. Observa cómo funciona el siguiente código:

for i in "Hola":
  print(i)

print("Fin")

# ## 4.4 Ejercicios

# Ahora puedes intentar hacer algunos de estos ejercicios sobre strings.
# 
# 1. Escribe un programa que, dado un string y un valor n no negativo, muestre por pantalla el string repetido n veces.
# 
# 2. Modifica el script anterior para que repita sólo los 3 primeros caracteres del string. La longitud mínima del string será de 3, si no, el programa mostrará un mensaje y terminará.
# 
# 3. Dado un string, muestra por pantalla un nuevo string que sea 3 copias de los últimos dos caracteres del string original. Lo longitud mínima del string será de 2, si no, el programa mostrará un mensaje y terminará.
# 
# 4. Dado un string, muestra por pantalla un nuevo string que tenga los dos últimos caracteres movidos al inicio. La longitud mínima del string será de 2.
# 
# 5. Dado un string, muestra por pantalla un nuevo string que sea el original, repitiendo cada caracter dos veces.
# 
# 6. Dados dos strings, muestra por pantalla la cantidad de veces que el segundo string aparece en el primero.
# 
# 7. Dados dos strings, muestra por pantalla un mensaje indicando si uno de los dos aparece al final del otro, ignorando diferencias de mayúsculas y minúsculas. Por ejemplo, el string "AbC" y "HiaBc" debería mostrar que si que aparece uno al final del otro.
# 
# 8. Realiza un script que genere 10 identificadores de socio aleatoriamente. Un identificador de socio está basado en 3 letras y 2 números del 0 al 9. Si se genera un identificador repetido, tendrá que generarse otro hasta que no salga repetido.
