# ----------------------------------------------------
# ----- ARCHIVO DE EJERCICIOS DEL COLLAB 02 -----
# ----------------------------------------------------
# Este archivo contiene todos los ejercicios de los
# cuadernos 02_01, 02_02 y 02_03.
# ----------------------------------------------------


# ---------------------------------------------
# ----- EJERCICIOS: SINTAXIS BÁSICA (02_01) -----
# ---------------------------------------------

# 1. Realiza un programa que calcule la suma de los números 43582134 y 1234567,
#    almacene el resultado en una variable, e imprima el resultado por pantalla.

# 2. Hoy en día, la tasa de cambio entre el euro y el dolar es de 0.85 euros por
#    cada dólar. Atendiendo a esta información, construye un programa que lea una
#    cantidad de dólares por teclado e informe al cliente de la cantidad de
#    euros que obtendría al cambiar.

# 3. Se cree comúnmente que 1 año humano equivale a 7 años en un perro.
#    Construye un programa que le pregunte al usuario en qué año nació y le
#    informe de su edad perruna. Asume que el año actual es 2021.


# ----------------------------------------------------------
# ----- EJERCICIOS: ESTRUCTURAS DE CONTROL (02_02) -----
# ----------------------------------------------------------

# --- Ejercicios de If/Else ---
# 1. Implementa un programa que lea la hora en formato 24 horas y lo convierta a
#    formato 12 horas. Como ejemplos de ejecución:
#
#    Introduce la hora: 8
#    Introduce los minutos: 57
#    Son las 08:57 AM
#
#    Introduce la hora: 21
#    Introduce los minutos: 31
#    Son las 09:31 PM
#
#    Introduce la hora: 26:
#    Hora inválida. Deben ser entre 0 y 23.
#
# 2. Se nos ha solicitado programar el calculador de la tarifa a pagar por los
#    usuarios de una compañía de telefonía móvil. Todos los usuarios pagan una
#    tarifa base de 10 euros al mes siempre que no hablen más de 180 minutos al
#    mes. A partir de los 180 minutos, los usuarios pagan 10 céntimos por cada
#    minuto hablado desde los 180 hasta los 240 minutos. A partir de ese
#    momento, los usuarios pagan 20 céntimos por cada minuto por cada minuto
#    extra consumido a partir de los 240. El calculador debe pedir al usuario
#    los minutos hablados y devolver los euros a pagar.
#
# 3. Otra persona y tú queréis reservar mesa en un restaurante. Queremos un
#    programa que nos pregunte el estilo de vestir nuestro y el de nuestro
#    compañero, que serán valores entre 0 y 10. Si uno de los dos tenemos un
#    estilo de 8 o superior, entonces sí que tendremos mesa para cenar y deberá
#    mostrar un mensaje por pantalla. Esto es así siempre y cuando uno de los
#    dos no tenga un 2, en cuyo caso no tendremos mesa. En cualquier otro caso,
#    el mensaje que debe mostrar es que no sabemos si tendremos mesa.
#
# 4. Realiza un programa que pregunte por un día de la semana y si estamos o no
#    de vacaciones. El programa deberá mostrar un mensaje indicando a qué hora
#    nos suena la alarma. Entre semana, la alarma sonará a las 8:00 y los fines
#    de semana a las 10:00. Sin embargo, si estamos de vacaciones, los días
#    entre semana sonará a las 10:00 y los fines de semana estará apagada.
#
# 5. Realiza un programa que pregunte tres valores enteros y muestre un mensaje
#    por pantalla indicando si los dos primeros tienen una diferencia máxima
#    de 1 mientras que el tercero tiene una diferencia mayor que 2 con los
#    otros dos. Utiliza la función abs(sum) para calcular el valor absoluto
#    de un número.

# --- Ejercicios de Bucles ---
# 1. Realiza un programa para calcular el factorial de un número entero
#    introducido por el teclado (sin utilizar la librería).
#
# 2. Implementa un juego que genere un número entero aleatorio entre 1 y 100.
#    Entonces, el usuario deberá introducir números por teclado para intentar
#    adivinar el número generado. Cada vez que el usuario introduzca un número
#    por teclado, el programa deberá determinar si el número es el generado
#    inicialmente (ganando el usuario la partida), si el número introducido por
#    el usuario es múltiplo o divisor del número (informando de que el número
#    introducido es múltiplo o divisor), o si no es ninguno de los otros dos
#    casos. Al final de la partida, el número de puntos obtenido por el usuario
#    es 100 menos el número de intentos del usuario. La puntuación debe
#    imprimirse al final del juego.


# ----------------------------------------------------------
# ----- EJERCICIOS: ESTRUCTURAS DE DATOS (02_03) -----
# ----------------------------------------------------------

# --- Ejercicios de Listas ---
# 1. Dada una lista de enteros, muestra por pantalla si un número introducido
#    por teclado está en la primera o en la última posición. La longitud mínima
#    de la lista será de 1, en caso contrario, el programa terminará.
#
# 2. Pide 4 números y añádelos a una lista. Después, rota los elementos y
#    guárdalos en una nueva lista (el último es el primero, etc.), mostrando
#    por pantalla esta nueva lista.
#
# 3. Dadas dos listas de longitudes diferentes, averiguar si el primero o el
#    último elemento de ambas listas es el mismo. En este caso, eliminar
#    dicho elemento y mostrar las listas resultantes.
#
# 4. Dada una lista de enteros, averiguar si el primer o el último elemento
#    es el mayor y sustituir el resto de elementos por éste (sin contar el
#    primero el último). Por ejemplo, la lista [11, 5, 9, 7] debería quedar
#    como [11, 11, 11, 7].
#
# 5. Calcular la cantidad de números impares que hay en una lista de enteros.
#
# 6. Dada una lista de enteros, mostrar por pantalla la diferencia entre el
#    mayor y el menor valor de la lista. Prueba a utilizar funciones del API
#    para obtener estos valores.
#
# 7. Dada una lista de enteros, devolver la media de todos los valores.
#    Prueba a buscar en el API.
#
# 8. Dada una lista de enteros, mostrar por pantalla si hay algún número que
#    esté repetido en dos posiciones consecutivas.
#
# 9. Dada una lista de enteros, elegir un número aleatorio de la lista.

# --- Ejercicios de Strings ---
# 1. Escribe un programa que, dado un string y un valor n no negativo, muestre
#    por pantalla el string repetido n veces.
#
# 2. Modifica el script anterior para que repita sólo los 3 primeros caracteres
#    del string. La longitud mínima del string será de 3, si no, el programa
#    mostrará un mensaje y terminará.
#
# 3. Dado un string, muestra por pantalla un nuevo string que sea 3 copias de
#    los últimos dos caracteres del string original. Lo longitud mínima del
#    string será de 2, si no, el programa mostrará un mensaje y terminará.
#
# 4. Dado un string, muestra por pantalla un nuevo string que tenga los dos
#    últimos caracteres movidos al inicio. La longitud mínima del string será
#    de 2.
#
# 5. Dado un string, muestra por pantalla un nuevo string que sea el original,
#    repitiendo cada caracter dos veces.
#
# 6. Dados dos strings, muestra por pantalla la cantidad de veces que el segundo
#    string aparece en el primero.
#
# 7. Dados dos strings, muestra por pantalla un mensaje indicando si uno de los
#    dos aparece al final del otro, ignorando diferencias de mayúsculas y
#    minúsculas. Por ejemplo, el string "AbC" y "HiaBc" debería mostrar que si
#    que aparece uno al final del otro.
#
# 8. Realiza un script que genere 10 identificadores de socio aleatoriamente.
#    Un identificador de socio está basado en 3 letras y 2 números del 0 al 9.
#    Si se genera un identificador repetido, tendrá que generarse otro hasta que
#    no salga repetido.
