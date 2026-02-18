################################################################################
#                                                                              #
#                   05_01_classes_and_objects.py                               #
#                                                                              #
################################################################################

# Una CLASE es una plantilla para crear objetos.
# Los OBJETOS (o instancias) son encarnaciones de una clase.

# --------------------------- Definición de una Clase ---------------------------
class Coche:
    # --- Atributo de clase ---
    # Es compartido por todas las instancias de la clase.
    ruedas = 4

    # --- Constructor (`__init__`) ---
    # Es un método especial que se llama al crear una nueva instancia.
    # `self` se refiere a la instancia que se está creando.
    def __init__(self, marca, modelo, color):
        # --- Atributos de instancia ---
        # Son específicos de cada objeto.
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        print(f"Se ha creado un coche {self.marca} {self.modelo}.")

    # --- Métodos ---
    # Son funciones que pertenecen a la clase. El primer parámetro siempre es `self`.
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche ahora va a {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"El coche ha reducido a {self.velocidad} km/h.")


# -------------------------- Creación y Uso de Objetos --------------------------
# "Instanciar" una clase es crear un objeto a partir de ella.
print("--- Creando objetos ---")
coche_de_ana = Coche("Renault", "Clio", "Rojo")
coche_de_juan = Coche("Ford", "Focus", "Azul")

# --- Acceso a atributos ---
# Se accede a los atributos de instancia y de clase con la notación de punto.
print(f"\nEl coche de Ana es un {coche_de_ana.marca} de color {coche_de_ana.color}.")
print(f"Todos los coches tienen {Coche.ruedas} ruedas.")
# También se puede acceder al atributo de clase desde la instancia
print(f"El coche de Juan también tiene {coche_de_juan.ruedas} ruedas.")


# --- Llamada a métodos ---
print("\n--- Usando los métodos de los objetos ---")
coche_de_ana.acelerar(50)
coche_de_juan.acelerar(30)
coche_de_ana.frenar(10)
