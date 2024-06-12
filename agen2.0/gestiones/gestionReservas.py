reservas = []

from gestionClientes import clienteExiste, obtenerNombreCliente
from gestionDestinos import destinoExiste, obtenerNombreDestino

def realizarReserva(codigoDestino, idCliente):
    if destinoExiste(codigoDestino) and clienteExiste(idCliente):
        reserva = {'codigo_destino': codigoDestino, 'id_cliente': idCliente}
        reservas.append(reserva)
        print(f'Reserva realizada para el cliente {idCliente} al destino {codigoDestino}.')
    else:
        print('Error: Código de destino o ID de cliente inválido.')

def cancelarReserva(codigoDestino, idCliente):
    reservaCancelada = False
    for reserva in reservas:
        if reserva['codigo_destino'] == codigoDestino and reserva['id_cliente'] == idCliente:
            reservas.remove(reserva)
            print(f'Reserva cancelada para el cliente {idCliente} al destino {codigoDestino}.')
            reservaCancelada = True
            break
    if not reservaCancelada:
        print('Error: Reserva no encontrada.')

def mostrarReservas():
    print('Reservas:')
    for reserva in reservas:
        nombreCliente = obtenerNombreCliente(reserva['id_cliente'])
        nombreDestino = obtenerNombreDestino(reserva['codigo_destino'])

        if nombreCliente and nombreDestino:
            print(f"Cliente: {nombreCliente} - Destino: {nombreDestino}")
