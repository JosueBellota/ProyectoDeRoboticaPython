# 02_02_control_structures.py
# Apuntes generados a partir de 02_Introducción_a_Python.ipynb
# ----------------------------------------------------------- 

# # 3 Estructuras de control y de repetición

# ## 3.1 If y Else

# Al igual que en otros lenguajes, en Python podemos expresar expresiones condicionales mediante estructuras ```if-else```. Python es un lenguaje que **no utiliza llaves** para separar bloques de código (i.e., *{}*) sino que se utilizan dos puntos (i.e., *:*)

# 
# Además de esto, mientras que en otros lenguajes de programación no es obligatorio que un bloque de código dentro de una estructura condicional, bucle, función o clase esté tabulado, **SÍ ES OBLIGATORIO** en Python. Si no, el programa no funcionará correctamente o simplemente lanzará error de interpretación. Para tabular el código en Python puedes utilizar o bien una tecla de tabulación o 4 espacios. Esto, a parte de quitar símbolos innecesarios, también favorece que el código sea más legible.
# 
# A nivel de guía de estilo, es preferible utilizar 4 espacios en vez de un tabulador, pero puedes utilizar lo que quieras. Eso sí, **NO DEBES MEZCLAR LOS DOS**. De esta forma, Python te obliga a tabular el código y aplicar buenas prácticas de programación.
# 
# En resumen, es necesario que las instrucciones de un bloque ```if``` y de un bloque ```else``` estén correctamente identadas.
# 
# A nivel de guía de estilo, también comentar que es recomendable que las instrucciones de cada bloque estén siempre en una línea diferente al propio ```if-else``` para facilitar la lectura.
# 
# A continuación tienes un ejemplo:

num = 7

if num >= 5:
  print("El número es mayor o igual a 5")
else:
  print("El número es menor que 5")

print("Esta línea se ejecuta siempre")

# Cuando queremos utilizar ```if-else``` anidados podemos emplear la instrucción ```elif``` que sirve como contracción. A continuación puedes ver dos ejemplos equivalentes. Presta atención a cómo se colocan las indentaciones con ```elif```:

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

# ## 3.2 Operaciones lógicas

# Los comparadores y operadores lógicos nos sirven para construir expresiones booleanas. Es decir, expresiones que se evaluarán a cierto o falso. Éstas son comunmente empleadas en las estructuras condicionales, así como condiciones de parada/continuar en los bucles. Al igual que otros lenguajes de programación, Python cuenta con los comparadores y operadores lógicos más comunmente empleados:
# 
# |    <br>Comparador    |    <br>Descripción                                                                                   |    <br>Ejemplos                                       |
# |--------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
# |    <br><           |    <br>Devuelve True si el   primer valor es<br>menor que el segundo valor proporcionado             |    <br>3 < 2<br>   <br>1 < 2<br>a < b                 |
# |    <br><=          |    <br>Devuelve True si el   primer valor es menor<br>o igual que el segundo valor proporcionado     |    <br>3 <= 2<br>2 <= 2<br>   <br>1 <= 2<br>a <= b    |
# |    <br>>           |    <br>Devuelve True si el   primer valor es mayor <br>que el segundo valor proporcionado            |    <br>3 > 2<br>1 > 2<br>a > b                        |
# |    <br>>=          |    <br>Devuelve True si el   primer valor es mayor <br>o igual que el segundo valor proporcionado    |    <br>3 >= 2<br>3 >= 3<br>1 >= 2<br>   <br>a >= b    |
# |    <br>==          |    <br>Devuelve True si los   dos valores son iguales                                                |    <br>3 == 3<br>4 == 5.2<br>a == b                   |
# |    <br>!=          |    <br>Devuelve True si los   dos valores son distintos                                              |    <br>3 != 3<br>4 != 5.2<br>a != b                   |
# 
# |    <br>Operador    |    <br>Descripción                                                                                         |    <br>Ejemplos                                                             |
# |--------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
# |    <br>and         |    <br>Devuelve True si ambas   expresiones se evalúan <br>a True y False en caso contrario.               |    <br>3 < 2 and 3 > 5   <br>3 < 2 and (3 % 2 ==   1)<br>2 < 3 and 5 > 3    |
# |    <br>or          |    <br>Devuelve True si alguna   de las dos expresiones <br>se evalúa a True y False en caso contrario.    |    <br>3 <= 2<br>2 <= 2<br>   <br>1 <= 2<br>a <= b                          |
# |    <br>not         |    <br>Devuelve True si la   expresión era falsa, <br>y False en caso contrario.                           |    <br>not 3 > 2<br>not 1 > 2<br>not a > b                                  |
# 
# A continuación, tienes algunos ejemplos:

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

# Si te ayuda, puedes utilizar paréntesis. A continuación tienes un ejemplo de cómo lo puedes utilizar. Sin ejecutar, ¿qué saldría por pantalla?

x = 6
y = 2

if x % 2 == 0 and (not ( x > 5 )):
  print("entro por if")
else:
  print("entro por else")

# ## 3.3 Ejercicios

# Con lo que has aprendido hasta ahora sobre Python, puedes intentar hacer algunos de estos ejercicios:
# 1.   Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas. Como ejemplos de ejecución:
# ```
# Introduce la hora: 8
# Introduce los minutos: 57
# Son las 08:57 AM
# Introduce la hora: 21
# Introduce los minutos: 31
# Son las 09:31 PM
# Introduce la hora: 26:
# Hora inválida. Deben ser entre 0 y 23.
# ```
# 2.   Se nos ha solicitado programar el calculador de la tarifa a pagar por los usuarios de una compañía de telefonía móvil. Todos los usuarios pagan una tarifa base de 10 euros al mes siempre que no hablen más de 180 minutos al mes. A partir de los 180 minutos, los usuarios pagan 10 céntimos por cada minuto hablado desde los 180 hasta los 240 minutos. A partir de ese momento, los usuarios pagan 20 céntimos por cada minuto por cada minuto extra consumido a partir de los 240. El calculador debe pedir al usuario los minutos hablados y devolver los euros a pagar.
# 
# 3. Otra persona y tú queréis reservar mesa en un restaurante. Queremos un programa que nos pregunte el estilo de vestir nuestro y el de nuestro compañero, que serán valores entre 0 y 10. Si uno de los dos tenemos un estilo de 8 o superior, entonces sí que tendremos mesa para cenar y deberá mostrar un mensaje por pantalla. Esto es así siempre y cuando uno de los dos no tenga un 2, en cuyo caso no tendremos mesa. En cualquier otro caso, el mensaje que debe mostrar es que no sabemos si tendremos mesa.
# 
# 4. Realiza un programa que pregunte por un día de la semana y si estamos o no de vacaciones. El programa deberá mostrar un mensaje indicando a qué hora nos suena la alarma. Entre semana, la alarma sonará a las 8:00 y los fines de semana a las 10:00. Sin embargo, si estamos de vacaciones, los días entre semana sonará a las 10:00 y los fines de semana estará apagada.
# 
# 
# 5. Realiza un programa que pregunte tres valores enteros y muestre un mensaje por pantalla indicando si los dos primeros tienen una diferencia máxima de 1 mientras que el tercero tiene una diferencia mayor que 2 con los otros dos. Utiliza la función abs(sum) para calcular el valor absoluto de un número.

# ## 3.4 While y For

# En Python tenemos dos tipos de estructuras de repeticion: bucles ```for``` y bucles ```while```. Podemos utilizar un ```while``` para aquellos casos donde queremos que se repita el bucle mientras se cumpla una determinada condición. La sintaxis es la siguiente:

i = 0

while i < 5:
  print(i)
  i+=1

# El bucle ```for``` lo utilizamos para repetir un bloque de instrucciones cuando sabemos la cantidad de veces que se deben repetir. La instrucción ```range(x)``` se repite desde un valor inicial de 0 hasta x - 1.

for i in range(10):
  print(i)

print("Fin")

# También podemos especificar el rango exacto mediante dos números separados por coma:

for i in range(1,10):
  print(i)

print("Fin")

# Esto mismo lo podemos hacer escribiendo los valores que queremos iterar:

for i in 1, 2, 3, "casa", "coche", 3.14:
  print(i)

print("Fin")

# ## 3.5 Ejercicios

# Puedes intentar hacer alguno de estos ejercicios:
# 
# 1. Realiza un programa para calcular el factorial de un número entero introducido por el teclado (sin utilizar la librería).  
# 2. Implementa un juego que genere un número entero aleatorio entre 1 y 100. Entonces, el usuario deberá introducir números por teclado para intentar adivinar el número generado. Cada vez que el usuario introduzca un número por teclado, el programa deberá determinar si el número es el generado inicialmente (ganando el usuario la partida), si el número introducido por el usuario es múltiplo o divisor del número (informando de que el número introducido es múltiplo o divisor), o si no es ninguno de los otros dos casos. Al final de la partida, el número de puntos obtenido por el usuario es 100 menos el número de intentos del usuario. La puntuación debe imprimirse al final del juego.
