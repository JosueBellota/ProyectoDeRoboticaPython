# 02_01_basics.py
# Apuntes generados a partir de 02_Introducción_a_Python.ipynb
# ----------------------------------------------------------- 

# **NOTA**: Si detectas algún error en este Colab, pon un mensaje en el foro para que lo podamos solucionar o envía un correo. 

# # 1 Escribiendo código Python

# La mayoría del código que editaremos en las prácticas de programación con Python será a través de un editor. Por tanto, una manera de organizar las distintas prácticas que realices, es creando ficheros .py dentro del mismo workspace, organizados en los directorios que quieras.
# 
# Ten en cuenta también, que antes de empezar con estas prácticas, deberás **activar** el entorno virtual:

# rosenv

# Después, abre el editor (p.e. VS Code), carga el workspace y crea los ficheros .py y/o directorios necesarios. Observa que tengas el entorno virutal cargado correctamente (es decir, que aparezca **rosenv** al inicio de la línea de comandos):
# 
# <figure style="text-align:center">
#   <center>
#   <img width = "60%" src="https://s3imagenes.s3.us-west-2.amazonaws.com/ejecucion.PNG"/>
#   <figcaption align="center">Entorno rosenv cargado</figcaption>
#   </center>
# </figure>

# ## 1.2 Guía de estilo de Python

# Cuando aprendemos un lenguaje, es conveniente tener en cuenta algunas recomendaciones de estilo. Aunque el objetivo de las prácticas de programación en Python no es hacer un código con un estilo perfecto, sí que iremos remarcando algunos aspectos y recomendaciones.
# 
# Si quieres escribir un código lo más correcto posible, es conveniente que le eches un ojo a la guía de estilo PEP 8: https://www.python.org/dev/peps/pep-0008/ 
# 
# El principio básico sería que *la legilidad es importante*. Para ser honestos, cuando empiezas a aprender Python y ves código escrito por gente más avanzada, parece complicado de leer. No obstante, según adquieras experiencia en el lenguaje, la consistencia de estilo será más aparente y cada vez encontrarás más fácil leer el código de otras personas.
# 
# A modo de curiosidad, prueba a abrir la consola de Python (escribiendo `python` en un terminal) y dentro de la consola escribe `import this`. Verás que te aparecen 19 aforismos llamados el Zen de Python que reflejan la filosofía de Python (aunque honestamente, se aplicarían a la mayoría de lenguajes).

# # 2 Sintaxis básica de Python

# ## 2.1 Tipos básicos y variables

# A diferencia de otros lenguajes de programación, las variables no tienen un tipo estático, sino que el tipo de una variable puede cambiar a lo largo de la ejecución del código. Por ejemplo, en un lenguaje dinámico, el siguiente bloque de código es perfectamente viable, mientras que en lenguajes estáticamente tipados como Java, esto sería imposible.

x = 5
x = "Hola"

# En Python, en el momento en el que asignas una variable, si no existe, se crea. Por tanto, en el bloque de código anterior, hemos creado y asignado dos valores a la variable x. En este sentido una variable no necesita ser previamente definida con un tipo para ser utilizada. Ojo, porque esto no implica que una variable pueda ser empleada para una evaluación sin ser definida. Por ejemplo, mira como el siguiente bloque de código fallaría al no estar definida la variable y e intentar imprimir el valor de la variable por el terminal.

# print(y) # Comentado porque provoca un error intencionado (NameError: name 'y' is not defined)

# Teniendo en cuenta esto, existen cuatro tipos básicos de valores: *int*, *float*, *string*, y *bool*:
# 
# |    <br>Tipo   de valor    |    <br>Descripción         |    <br>Ejemplos   de uso                                  |
# |---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
# |    <br>int                |    <br>Valor numérico de tipo entero                                                                                                                                                                                 |    <br>x = 23                                             |
# |    <br>float              |    <br>Valor numérico de tipo coma flotante o decimal                                                                                                                                                                |    <br>y = 11.34                                          |
# |    <br>string             |    <br>Sirve para representar valores de tipo texto (i.e., cadenas). <br><br>Para representar cadenas de texto se emplazan o bien entre <br><br>comillas simples o bien entre comillas dobles, pero no mezcladas.    |    <br>c = '¡Hola Mundo!'<br>   <br>c2 = "¡Hola Mundo!"    |
# |    <br>bool               |    <br>Únicamente puede tomar dos valores True (algo que es cierto) <br><br>y False (algo que es falso)                                                                                                              |    <br>a = True<br>   <br>b = False                       |

#La variable x es de tipo int y la y de tipo float
x = 10
y = 3.5

#También podemos hacer un casting para convertir un número o string a int (o a otros tipos)
print(int(y))
print(int("345"))

# El tipo boolean tiene dos posibles valores: True y False (con mayúscula). Al igual que otros lenguajes, el valor 0 se castea como False y cualquier valor distinto de 0 como True:

a = True

print(a)
print(bool(0))
print(bool(1))
print(bool(-5))

# La función `type()` nos devuelve el tipo de una variable pasada por parámetro:

x = 5
print(type(x)) # En script necesitamos print para ver el resultado

# Aunque llegados a este punto ya te habrás dado cuenta, para poner un comentario en Python, utilizaremos el caracter ```# ```

# Esto es un comentario

# También podemos hacer comentarios multilínea mediante comentarios llamados *docstring*. Estos comentarios van enmarcados entre triples comillas ``` """ ```:

""" Esto sería un comentario
de varias líneas
"""

# Si estamos utilizando Python 2 y ponemos acentos, es posible que nos salga un error diciendo que hay caracteres no ASCII. Esto ocurre porque se asume que sólo se utiliza ASCII. Si utilizamos Python 3 no habrá problema puesto que utiliza UTF8 para codificar los ficheros. Para solucionar este problema de Python 2, a parte de guardar el fichero con extensión .py y codificación UTF8, debemos poner la siguiente línea al inicio del script:

# encoding: utf-8

# ## 2.2 Operaciones aritméticas

# Al igual que en otros lenguajes de programación, en Python contamos con una serie de operaciones aritméticas que podemos realizar sobre valores numéricos:
# 
# |    <br>Operador    |    <br>Descripción                                                            |    <br>Ejemplo                              |
# |--------------------|-------------------------------------------------------------------------------|---------------------------------------------|
# |    <br>+           |    <br>Suma dos valores                                                       |    <br>a = 1 + 23.4<br>   <br>b = a + 33    |
# |    <br>-           |    <br>Resta dos valores                                                      |    <br>a = 5 – 7<br>   <br>b = a – 11.2     |
# |    <br>*           |    <br>Multiplicación de dos valores                                          |    <br>a = 3 * 4<br>   <br>b = a * 1.2      |
# |    <br>/           |    <br>División decimal de dos valores. Siempre   retorna un valor decimal    |    <br>a = 4 / 2<br>   <br>b = a / 1.3      |
# |    <br>//          |    <br>División entera de dos valores. Siempre   retorna un valor entero      |    <br>a = 9 // 3<br>   <br>b = a // 2      |
# |    <br>%           |    <br>Retorna el resto de la división entre dos   valores                    |    <br>a = 3 % 2<br>   <br>                 |
# |    <br>`**`          |    <br>Realiza la potenciación de un valor a otro                             |    <br>a = 4`**`2<br>   <br>b = a**(2)          |

# La guía de estilo recomienda poner un espacio entre los operadores, prefiriendo `num = 10` y no `num=10`. También recomienda que los nombres de las variables sean en minúsculas, prefiriendo `unit_price` a `unitPrice`.

# ## 2.3 Entrada/salida

# Si queremos mostrar información por pantalla utilizaremos la función ```print()```. Esta función puede aceptar varios argumentos separados por comas.

print("Mensaje sin variable")

x = 5

#Dos formas diferentes de hacer el print en Python 3
print("El valor es "+str(x)) #un int no puede imprimirse si no lo convertimos a string previamente
print("El valor es ", x)

# También tenemos una tercera forma para imprimir información por pantalla mediante marcas de interpolación. Las marcas pueden modificarse para controlar el aspecto de la información. El formato de una marca en términos generales está formado de dos partes ```{campo.formato}```:
# 
# * **Campo**: número que identifica el número de argumento que se desea interpolar en la cadena.
# * **Formato**: Define el formato del argumento a interpolar mediante la siguiente forma donde cada elemento entre corchetes es opcional.

x = 5
a = x/3

print("El valor es {0} y si queremos otro valor sería así {1}".format(x, x/3)) #dentro de format ponemos los valores en orden que queremos imprimir
print("El valor es {1} y si queremos otro valor sería así {0}".format(x, x/3)) #podemos cambiar el orden
print("El valor es {0} y si queremos otro valor sería así {a}".format(x, a=x/3)) #... y utilizar variables
print("El valor es {0:.3f} y si queremos otro valor sería así {a:.2f}".format(x, a=x/3)) #... y si queremos formatear los decimales de la salida

#Si queremos en Python 2
#print "Esto sería sin paréntesis"

# Si queremos introducir datos por teclado, podemos utilizar la función `input()`. Esta función nos permite mostrar un texto al usuario y almacenar el valor introducido en una variable en formato string. Si queremos que se almacene en otros tipos de datos, debemos hacer un casting sobre ello, mediante funciones como ```float()``` o ```int()```:

print("\n--- Inicio de sección interactiva (input) ---")
a = int(input("Introduce el radio (int):")) #a es de tipo int

b = float(input("Introduce el radio (float):")) #b es de tipo float

a = b #a cambia a float

a = "Ahora pasa a ser una cadena" #a cambia a cadena

#Mira este ejemplo donde combinamos entrada con varias maneras de mostrar la salida
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

sum = num1 + num2

print("El resultado de sumar ",num1," y ",num2," es ",sum)
print("El resultado de sumar {0} y {1} es {2}".format(num1, num2, sum))
print("El resultado de sumar "+str(num1)+" y "+str(num2))
print("--- Fin de sección interactiva ---\\n")

# ## 2.4 Módulos

# Python está estructurado en módulos que son archivos que contienen definiciones de funciones y declaraciones ejecutables de Python. Esto nos permite utilizar funciones y clases definidas por los módulos importados.
# 
# Para importar un módulo debemos utilizar la palabra ```import``` seguida del nombre del módulo. Por ejemplo, el módulo ```math``` nos ofrece varias funciones matemáticas, como por ejemplo, la raíz cuadrada.
# 
# Para acceder a las funciones del módulo escribiremos el nombre del módulo seguido de un punto y la función que queremos utilizar: ```modulo.funcion```. Fíjate en el siguiente ejemplo para ver cómo podemos importar el módulo y utilizar la función ```sqrt```:

import math

x = 10
print("La raíz cuadrada de", x, "es", math.sqrt(x))

# Math es el módulo matemático con funciones como sin, cos, tan, exp, ceil, floor, log, etc.: https://docs.python.org/3/library/math.html
# 
# En ocasiones es conveniente acceder a la propia documentación de un módulo para examinar qué funciones ofrece. Una forma de realizar esto es mediante la función ```help()```:

# help(math) # Comentado para no llenar la consola de texto de ayuda

# También podemos utilizar el ```help``` para una función concreta:

# help(math.factorial)

# Existe otra forma de importar una función y así evitar tener que escribir el nombre del módulo cada vez:

from math import factorial

print(factorial(10))

# También hay una tercera forma que nos permite renombrar el módulo. Algo que puede ser beneficioso en ciertas ocasiones por cuestiones de legibilidad:

from math import factorial as fac

print(fac(10))

# Se puede importar más de una función (o todas con el símbolo "*") en la misma sentencia, aunque no seguiría la guía de estilo:

from math import sin
from math import sin, cos #lo recomendable, según la guía de estilo, sería en dos líneas separadas
from math import *

# Otros módulos que te serán de utilidad son **sys**, que es el módulo del sistema para acceder al sistema operativo y constantes, y también **robot_control_class** que es el módulo de ROS. Puedes acceder a la documentación de la lista completa de módulos para Python 3.8 en https://docs.python.org/3.8/py-modindex.html

# ## 2.5 Ejercicios

# Ahora, para calentar motores, puedes intentar hacer algunos de los siguientes ejercicios:
# 1.   Realiza un programa que calcule la suma de los números 43582134 y 1234567, almacene el resultado en una variable, e imprima el resultado por pantalla.
# 2.   Hoy en día, la tasa de cambio entre el euro y el dolar es de 0.85 euros por cada dólar. Atendiendo a esta información, construye un programa que lea una cantidad de dólares por teclado e informe al cliente de la cantidad de euros que obtendría al cambiar.
# 3.   Se cree comúnmente que 1 año humano equivale a 7 años en un perro. Construye un programa que le pregunte al usuario en qué año nació y le informe de su edad perruna. Asume que el año actual es 2021.
