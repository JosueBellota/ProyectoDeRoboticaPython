# 03_05_dictionaries.py

# Diccionarios: Estructuras clave-valor (dict)

# Creación
dic_vacio = {}
contactos = {123: "Juan", 456: "Maria", 789: "Pedro"}
print(f"Diccionario inicial: {contactos}")

# Acceso
print(f"Contacto 456: {contactos[456]}")
# .get() es más seguro porque no da error si la clave no existe (devuelve None o un defecto)
print(f"Contacto inexistente (get): {contactos.get(999, 'No encontrado')}")

# Añadir o Modificar
contactos[122] = "Eva"      # Añade nuevo
contactos[123] = "Juanito"  # Modifica existente
contactos.update({124: "Manolo", 789: "Peter"}) # Actualización múltiple
print(f"Tras modificaciones: {contactos}")

# Eliminar
del contactos[456]
valor_eliminado = contactos.pop(789)
print(f"Tras borrar 456 y 789 (era {valor_eliminado}): {contactos}")

# Comprobaciones
print(f"¿Existe la clave 123? {123 in contactos}")
print(f"Tamaño: {len(contactos)}")

# Recorrer diccionarios
print("--- Recorrido ---")
for nif, nombre in contactos.items():
    print(f"NIF: {nif} -> Nombre: {nombre}")

# Diccionarios anidados (Estructuras más complejas)
usuarios = {
    "user1": {"nombre": "Paco", "email": "paco@mail.com", "vip": True},
    "user2": {"nombre": "Ana", "email": "ana@mail.com", "vip": False}
}
print(f"Email de user1: {usuarios['user1']['email']}")
