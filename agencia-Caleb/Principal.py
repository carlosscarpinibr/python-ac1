# programa_principal.py

from gestiones.gestionClientes import (
    anadirCliente,
    clienteExiste,
    obtenerNombreCliente,
    mostrarClientes,
    clientes
)
from gestiones.gestionDestinos import (
    anadirDestino,
    destinoExiste,
    obtenerNombreDestino,
    mostrarDestinos,
    destinos
)

reservas = []

# Función para realizar una reserva
def realizarReserva(codigoDestino, idCliente):
    if destinoExiste(codigoDestino) and clienteExiste(idCliente):
        reserva = {'codigo_destino': codigoDestino, 'id_cliente': idCliente}
        reservas.append(reserva)
        print(f'Reserva realizada para el cliente {idCliente} al destino {codigoDestino}.')
    else:
        print('Error: Código de destino o ID de cliente inválido.')

# Función para cancelar una reserva
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

# Función para mostrar todas las reservas
def mostrarReservas():
    print('Reservas:')
    for reserva in reservas:
        nombreCliente = obtenerNombreCliente(reserva['id_cliente'])
        nombreDestino = obtenerNombreDestino(reserva['codigo_destino'])

        if nombreCliente and nombreDestino:
            print(f"Cliente: {nombreCliente} - Destino: {nombreDestino}")

# Función principal para ejecutar el programa
def main():
    while True:
        print("\n1. Añadir destino")
        print("2. Añadir cliente")
        print("3. Realizar reserva")
        print("4. Cancelar reserva")
        print("5. Mostrar destinos")
        print("6. Mostrar clientes")
        print("7. Mostrar reservas")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = int(input("Ingrese el código del destino: "))
            nombre = input("Ingrese el nombre del destino: ")
            precio = float(input("Ingrese el precio del destino: "))
            anadirDestino(codigo, nombre, precio)
        
        elif opcion == '2':
            idCliente = int(input("Ingrese el ID del cliente: "))
            nombre = input("Ingrese el nombre del cliente: ")
            anadirCliente(idCliente, nombre)
        
        elif opcion == '3':
            codigoDestino = int(input("Ingrese el código del destino: "))
            idCliente = int(input("Ingrese el ID del cliente: "))
            realizarReserva(codigoDestino, idCliente)
        
        elif opcion == '4':
            codigoDestino = int(input("Ingrese el código del destino: "))
            idCliente = int(input("Ingrese el ID del cliente: "))
            cancelarReserva(codigoDestino, idCliente)
        
        elif opcion == '5':
            mostrarDestinos()
        
        elif opcion == '6':
            mostrarClientes()
        
        elif opcion == '7':
            mostrarReservas()
        
        elif opcion == '8':
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
