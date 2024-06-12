from obtenerDestino.obtenerDestino import obtener_destino
from obtenerCliente.obtenerCliente import obtener_cliente
# Lista para almacenar reservas
reservas = []
def realizar_reserva(reservas):
    """
    Solicita al usuario los datos para realizar una reserva y la añade a la lista de reservas.

    Parámetros:
    None

    Retorno:
    None
    """
    codigo_destino = input("Ingrese el código del destino: ")
    id_cliente = input("Ingrese el ID del cliente: ")

    destino = obtener_destino(codigo_destino)
    cliente = obtener_cliente(id_cliente)

    if destino and cliente:
        reserva = {'destino': destino, 'cliente': cliente}
        reservas.append(reserva)
        print(f"Reserva realizada: Cliente {cliente['nombre']} en Destino {destino['nombre']}")
    else:
        print("Destino o cliente no encontrado. Reserva no realizada.")

if __name__ == "__main__":
    realizar_reserva()
