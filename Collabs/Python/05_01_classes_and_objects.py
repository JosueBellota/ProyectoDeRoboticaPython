# 05_01_classes_and_objects.py

# En Python, las clases se definen con 'class' y usan PascalCase
class Persona:
    """ Creamos una nueva persona con un nombre y una edad """
    unidad_masa = "kg" # Atributo de clase

    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def mostrar(self):
        print("El nombre es ", self.nombre, " y la edad es ", self.edad)

# Instanciación y uso
p = Persona("Juan", 25)
print("El nombre de p es ", p.nombre, " y la edad es ", p.edad)
p.mostrar()

def matching_list(dict, value):
  matchings = []
  for item in dict:
    if dict[item] == value:
      matchings.append(item)

  if len(matchings) != 0:
    return len(matchings)
  else:
    return None

pairs = {"item1" : "coche", "item2" : "moto", "item3" : "bicicleta"}

res = matching_list(pairs, "moto")
if res is not None:
  print("Se han encontrado "+str(res)+" elementos")
else:
  print("No hay ningún item que coincida")
