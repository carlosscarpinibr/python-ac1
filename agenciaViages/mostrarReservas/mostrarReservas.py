from realizarReserva.realizarReserva import realizar_reserva
from cancelarReserva.cancelarReserva import cancelar_reserva
# Lista para almacenar reservas
reservas = []
def mostrar_reservas():
    """
    Muestra todas las reservas.
    
    Parámetros:
    None

    Retorno:
    None
    """
    if not reservas:
        print("No hay reservas.")
    else:
        print("Lista de reservas:")
        for reserva in reservas:
            print(f"Cliente: {reserva['cliente']['nombre']}, Destino: {reserva['destino']['nombre']}")

# Funciones de prueba para demostrar el funcionamiento
if __name__ == "__main__":
    while True:
        print("\n1. Realizar reserva")
        print("2. Cancelar reserva")
        print("3. Mostrar reservas")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            realizar_reserva()
        elif opcion == '2':
            cancelar_reserva()
        elif opcion == '3':
            mostrar_reservas()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
    
