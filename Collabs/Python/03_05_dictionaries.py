################################################################################
#                                                                              #
#                        03_05_dictionaries.py                                 #
#                                                                              #
################################################################################

# Colecciones de pares clave-valor. Son mutables y no tienen un orden garantizado
# (aunque en versiones recientes de Python recuerdan el orden de inserción).

# ------------------------- Creación de Diccionarios -------------------------
contactos = {
    12345678: "Juan Pérez",
    "user_admin": "Maria Garcia",
}
print("Diccionario:", contactos)


# -------------------------- Acceso a los Valores --------------------------
# Con corchetes `[]` (da error si la clave no existe).
print("\nAcceso con [12345678]:", contactos[12345678])

# Con `.get()` (devuelve `None` o un valor por defecto si la clave no existe).
print("Acceso con .get('user_admin'):", contactos.get("user_admin"))
print("Acceso a clave inexistente con .get():", contactos.get(9999, "No encontrado"))


# ---------------------- Añadir y Modificar Elementos ----------------------
# Si la clave no existe, se añade. Si existe, se actualiza el valor.
contactos[11223344] = "Ana Martín"  # Añadir
contactos[12345678] = "Juan Pérez Gómez"  # Modificar
print("\nDiccionario modificado:", contactos)

# `.update()` añade o modifica múltiples elementos.
contactos.update({"user_admin": "Maria García López", "new_user": "Eva Ramos"})
print("Tras update():", contactos)


# ------------------------- Eliminar Elementos -------------------------
# `del` elimina el par clave-valor.
del contactos[11223344]
print("\nDespués de `del`:", contactos)

# `.pop()` elimina el par y devuelve el valor.
valor_eliminado = contactos.pop("new_user")
print(f"Tras `.pop()` (valor devuelto: '{valor_eliminado}'):", contactos)


# --------------------- Comprobaciones y Utilerías ---------------------
# Comprobar si una clave existe.
print("\n'user_admin' in contactos:", "user_admin" in contactos)

# Obtener número de pares.
print("Tamaño:", len(contactos))


# ----------------------- Recorrer un Diccionario -----------------------
print("\nRecorriendo con .items():")
for clave, valor in contactos.items():
    print(f"  - {clave}: {valor}")

# También se puede iterar sobre .keys() o .values()


# ------------------------- Diccionarios Anidados -------------------------
usuarios = {
    "user1": {"nombre": "Paco", "email": "paco@mail.com"},
    "user2": {"nombre": "Ana", "email": "ana@mail.com"},
}
print("\nEmail del user1:", usuarios["user1"]["email"])
