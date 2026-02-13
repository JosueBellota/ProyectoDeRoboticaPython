# 05_02_visibility_and_str.py

# Definimos una clase Persona
class Persona:
  def __init__(self, n, e):
    self.nombre = n #público
    self.__edad = e #privado

  def mostrar(self): #público
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)

  def __mostrar(self): #privado
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)

  def __str__(self):
    return "El nombre es "+self.nombre+" y la edad es "+str(self.__edad)

p = Persona("Juan", 25)
print("El nombre es "+p.nombre)
p.mostrar()

# Descomentar las siguientes líneas para ver los errores de acceso a atributos/métodos privados
# print("La edad es "+p.__edad) # Esto fallará
# p.__mostrar() # Esto fallará

print("
Usando __str__:")
print(p)
