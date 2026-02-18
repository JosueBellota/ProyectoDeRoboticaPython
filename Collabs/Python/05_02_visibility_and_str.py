################################################################################
#                                                                              #
#                   05_02_visibility_and_str.py                                #
#                                                                              #
################################################################################

# Este fichero explica el concepto de visibilidad (atributos privados) y
# el uso del método especial `__str__`.

# --- Convenciones de Visibilidad en Python ---
# A diferencia de otros lenguajes, Python no tiene un sistema estricto de
# "privado" o "público". En su lugar, usa convenciones basadas en guiones bajos.

class MiClase:
    def __init__(self):
        # Atributo público: accesible desde cualquier lugar.
        self.publico = "Soy público"
        
        # Atributo "protegido" (convención): No debería ser modificado desde fuera.
        self._protegido = "Soy para uso interno de la clase"
        
        # Atributo "privado" (name mangling): Python cambia el nombre internamente.
        self.__privado = "Soy 'privado', mi nombre se ha modificado"

    def _metodo_protegido(self):
        print("Este método es para uso interno.")

    def __metodo_privado(self):
        print("Este método es 'privado'.")
    
    def get_privado(self):
        return self.__privado
    
    def llamar_privado(self):
        self.__metodo_privado()

# --- Prueba de acceso ---
obj = MiClase()
print("--- Visibilidad ---")
print(obj.publico)       # OK
print(obj._protegido)    # OK, pero no se debería hacer por convención.
# print(obj.__privado)     # AttributeError: No existe un atributo con ese nombre.
print(obj.get_privado()) # OK, a través de un método público.
obj.llamar_privado()     # OK, llamado desde dentro de la clase.

# Python deforma el nombre de los atributos `__` para que no colisionen.
# Se puede acceder, pero es una muy mala práctica.
# print(obj._MiClase__privado) # Esto funcionaría.


# -------------------- El método especial `__str__` --------------------
# Este método define la representación "informal" o amigable de un objeto como un string.
# Se invoca automáticamente al usar `print(objeto)` o `str(objeto)`.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # --- Sin `__str__` ---
    # Si no se define, print() muestra una representación por defecto poco útil.

    # --- Con `__str__` ---
    def __str__(self):
        """Devuelve un string descriptivo de la instancia."""
        return f"Persona(Nombre: {self.nombre}, Edad: {self.edad})"

# --- Prueba ---
p1 = Persona("Ana", 30)

print("\n--- Método __str__ ---")
print("Imprimiendo el objeto directamente:")
print(p1) # Llama a p1.__str__()

# Es equivalente a:
representacion_str = str(p1)
print("\nResultado de str(objeto):")
print(representacion_str)
