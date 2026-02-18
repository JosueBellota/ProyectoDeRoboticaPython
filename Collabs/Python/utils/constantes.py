# Este es el fichero: constantes.py

"""
Este fichero sirve como un lugar centralizado para guardar constantes
que pueden ser usadas a lo largo de una aplicación.
"""

# Por convención, los nombres de las constantes se escriben en mayúsculas.
PI = 3.14159
GRAVEDAD = 9.81
URL_API_PRODUCCION = "https://api.ejemplo.com/v1"


# También se pueden agrupar constantes relacionadas dentro de una clase,
# que actúa como un "espacio de nombres" (namespace).
class EstadoUsuario:
    """Clase que agrupa constantes de estados de usuario."""
    PENDIENTE = "PENDIENTE"
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    BANEADO = "BANEADO"
