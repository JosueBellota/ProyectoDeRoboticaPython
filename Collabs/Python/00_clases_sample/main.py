from auto import Auto
from moto import Moto
from dueño import Dueño

def main():
    """
    Función principal para demostrar el uso de las clases,
    herencia y polimorfismo.
    """
    print("--- Creación de Vehículos ---")
    # Crear instancias de las clases hijas
    mi_auto = Auto("Toyota", "Corolla", 2022, 4, "Gasolina")
    mi_moto = Moto("Honda", "CBR500R", 2023, 500)

    # Imprimir información usando el método polimórfico mostrar_info
    print(mi_auto.mostrar_info())
    print(mi_moto.mostrar_info())
    print("-" * 20)


    print("--- Probando Métodos Específicos ---")
    # Usar métodos específicos de cada clase
    print(mi_auto.abrir_maletero())
    print(mi_moto.hacer_wheelie())
    print("-" * 20)


    print("--- Demostración de Polimorfismo ---")
    # Lista de vehículos (objetos de diferentes clases pero con un padre común)
    vehiculos = [mi_auto, mi_moto]

    # Iterar y llamar a métodos comunes
    for vehiculo in vehiculos:
        print(f"Interactuando con: {vehiculo.marca} {vehiculo.modelo}")
        print(vehiculo.encender())
        # Llamar al método polimórfico 'mover'
        print(vehiculo.mover(50))
        print(vehiculo.apagar())
    print("-" * 20)


    print("--- Creación y Asociación con Dueño ---")
    # Crear un dueño
    propietario = Dueño("Alex", "Calle Falsa 123")

    # Asociar vehículos al dueño
    propietario.comprar_vehiculo(mi_auto)
    propietario.comprar_vehiculo(mi_moto)

    print("")
    # Mostrar los vehículos del dueño
    propietario.mostrar_vehiculos()
    print("-" * 20)

if __name__ == "__main__":
    main()
