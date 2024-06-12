from gestiones.gestionClientes import anadirCliente, mostrarClientes
from gestiones.gestionDestinos import anadirDestino, mostrarDestinos
from gestiones.gestionReservas import realizarReserva, cancelarReserva, mostrarReservas

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
