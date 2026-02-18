################################################################################
#                                                                              #
#                       05_06_practice.py (Solutions)                          #
#                                                                              #
################################################################################

# --- 1. Clase Básica y método `__str__` ---
# Crea una clase `Libro` con atributos `titulo` y `autor`.
# Añade un método `__str__` que devuelva "TITULO por AUTOR".
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'

# --- Prueba ---
libro_1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien")
print(f"1. Libro creado: {libro_1}")


# --- 2. Atributos "Privados" y Métodos ---
# Crea una clase `CuentaBancaria` con un atributo `__saldo` (privado).
# Añade métodos `depositar(cantidad)`, `retirar(cantidad)` y `get_saldo()`.
# El método `retirar` no debe permitir que el saldo sea negativo.
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    
    def get_saldo(self):
        return self.__saldo
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Error: Retiro no válido o fondos insuficientes.")

# --- Prueba ---
print("
--- 2. Cuenta Bancaria ---")
mi_cuenta = CuentaBancaria(1000)
print(f"Saldo inicial: {mi_cuenta.get_saldo()}€")
mi_cuenta.depositar(500)
print(f"Saldo tras depósito: {mi_cuenta.get_saldo()}€")
mi_cuenta.retirar(200)
print(f"Saldo tras retiro: {mi_cuenta.get_saldo()}€")
mi_cuenta.retirar(2000) # Esto mostrará un error


# --- 3. Herencia y Sobrescritura de Métodos ---
# Crea una clase `Animal` con un método `sonido()` que devuelva "Sonido genérico".
# Crea una subclase `Perro` que herede de `Animal` y sobrescriba el método
# `sonido()` para que devuelva "Guau!".
class Animal:
    def sonido(self):
        return "Sonido genérico de animal"

class Perro(Animal):
    def sonido(self):
        return "Guau!"

# --- Prueba ---
print("
--- 3. Herencia ---")
animal_generico = Animal()
bobby = Perro()
print(f"Sonido de un animal: {animal_generico.sonido()}")
print(f"Sonido de un perro: {bobby.sonido()}")


# --- 4. Métodos de Clase y Estáticos ---
# Crea una clase `Mate` con:
# - Un método estático `es_par(numero)`.
# - Un método de clase `descripcion()` que devuelva "Clase de utilidades matemáticas".
class Mate:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0
    
    @classmethod
    def descripcion(cls):
        # cls se refiere a la clase Mate
        return "Clase de utilidades matemáticas."

# --- Prueba ---
print("
--- 4. Métodos Estáticos y de Clase ---")
print(f"¿Es 4 par? {Mate.es_par(4)}")
print(f"¿Es 7 par? {Mate.es_par(7)}")
print(f"Descripción de la clase: {Mate.descripcion()}")
