class Coche:
    """ Define un vehículo con marca y modelo """
    
    # Declaración de variables de clase/tipado antes del constructor
    __marca = str
    __modelo = str

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def obtener_descripcion(self):
        return f"{self.__marca} {self.__modelo}"


class Transporte:
    """ Clase que gestiona un servicio de transporte usando un Coche privado """

    # Atributos de clase siguiendo el convenio solicitado
    __id_servicio = int
    __tipo_ruta = str
    # Aquí es donde 'Coche' es un parámetro que se guardará de forma privada
    __vehiculo = Coche 

    def __init__(self, id_servicio, tipo_ruta, coche_asignado):
        """
        Constructor que recibe una instancia de Coche y la privatiza
        dentro de la lógica de Transporte.
        """
        self.__id_servicio = id_servicio
        self.__tipo_ruta = tipo_ruta
        
        # Guardamos la instancia de la otra clase como atributo privado
        if isinstance(coche_asignado, Coche):
            self.__vehiculo = coche_asignado
        else:
            print("Error: El parámetro debe ser una instancia de la clase Coche")

    def mostrar_detalles_viaje(self):
        """ Accede al objeto privado __vehiculo para obtener su información """
        nombre_coche = self.__vehiculo.obtener_descripcion()
        return (f"Servicio #{self.__id_servicio} ({self.__tipo_ruta}). "
                f"Vehículo asignado: {nombre_coche}")

    def get_id(self):
        return self.__id_servicio

# --- Ejemplo de Uso ---

# 1. Creamos la instancia de la clase que será "parámetro"
mi_tesla = Coche("Tesla", "Model S")

# 2. Creamos la instancia de Transporte pasando el objeto Coche
logistica_premium = Transporte(101, "Urbana", mi_tesla)

# 3. Acceso a través de la interfaz pública
print(logistica_premium.mostrar_detalles_viaje())

# 4. Intento de acceso directo al objeto privado (fallará)
try:
    print(logistica_premium.__vehiculo.obtener_descripcion())
except AttributeError:
    print("\n[Aviso]: No se puede acceder a '__vehiculo' directamente, es privado.")