################################################################################
#                                                                              #
#               05_03_inheritance_polymorphism.py                              #
#                                                                              #
################################################################################

# --- 1. Herencia ---
# La herencia permite que una clase (subclase o clase hija) adquiera los
# atributos y métodos de otra clase (superclase o clase padre).

# --- Clase Padre (Superclase) ---
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        return f"Soy un vehículo de marca {self.marca}."

# --- Clase Hija (Subclase) ---
# Se especifica la clase padre entre paréntesis.
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        # `super()` llama a los métodos de la clase padre.
        # Aquí, llamamos al constructor del padre para inicializar `marca`.
        super().__init__(marca)
        self.modelo = modelo  # Atributo propio de la subclase

    # --- Sobrescritura de método ---
    # Se redefine un método de la clase padre para que se comporte diferente.
    def describir(self):
        return f"Soy un coche {self.marca} {self.modelo}."

# --- Prueba de Herencia ---
print("--- 1. Herencia ---")
vehiculo_generico = Vehiculo("Genérica")
mi_coche = Coche("Ford", "Mustang")

print(vehiculo_generico.describir())
print(mi_coche.describir()) # Llama al método sobrescrito en Coche


# --- 2. Polimorfismo ---
# "Poli" = muchas, "morfismo" = formas.
# Es la capacidad de usar una misma interfaz (función o método) para
# tratar objetos de diferentes clases.

class Moto(Vehiculo):
    # No sobrescribe el método describir, por lo que usará el del padre.
    pass

# Esta función funciona con cualquier objeto que sea un "Vehiculo" o herede de él.
def imprimir_descripcion(vehiculo):
    # No necesita saber si es un Coche, una Moto o un Vehiculo, solo que tiene
    # un método `describir()`.
    print(vehiculo.describir())

# --- Prueba de Polimorfismo ---
print("\n--- 2. Polimorfismo ---")
moto_de_ana = Moto("Honda")
imprimir_descripcion(mi_coche)      # Funciona con un objeto Coche
imprimir_descripcion(moto_de_ana)   # Funciona con un objeto Moto


# --- 3. Duck Typing ---
# "Si camina como un pato y grazna como un pato, entonces debe ser un pato."
# En Python, no nos importa la clase de un objeto, sino qué puede hacer (qué
# métodos tiene). No es necesario que hereden de una clase común.

class Pato:
    def hablar(self):
        return "Cuac!"

class Persona:
    def hablar(self):
        return "¡Hola!"

# Esta función no pide una clase específica, solo un objeto que tenga un método `hablar()`.
def hacer_hablar(entidad_parlante):
    print(entidad_parlante.hablar())

# --- Prueba de Duck Typing ---
print("\n--- 3. Duck Typing ---")
donald = Pato()
juan = Persona()

hacer_hablar(donald)  # Funciona porque Pato tiene el método `hablar`
hacer_hablar(juan)    # Funciona porque Persona también tiene el método `hablar`
