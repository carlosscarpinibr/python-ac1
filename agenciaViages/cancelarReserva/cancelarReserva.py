
# Lista para almacenar reservas
reservas = []

def cancelar_reserva():
    """
    Solicita al usuario los datos para cancelar una reserva existente.

    Parámetros:
    None

    Retorno:
    None
    """
    codigo_destino = input("Ingrese el código del destino: ")
    id_cliente = input("Ingrese el ID del cliente: ")

    reserva_encontrada = False
    for reserva in reservas:
        if reserva['destino']['codigo'] == codigo_destino and reserva['cliente']['id'] == id_cliente:
            reservas.remove(reserva)
            print(f"Reserva cancelada: Cliente {reserva['cliente']['nombre']} en Destino {reserva['destino']['nombre']}")
            reserva_encontrada = True
            break

    if not reserva_encontrada:
        print("Reserva no encontrada. No se puede cancelar.")