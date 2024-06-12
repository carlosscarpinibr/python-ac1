# Archivo principal:
#importará y utilizará las funciones definidas en los módulos anteriores:

import gestionar
import reservas

def main():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestionar destinos")
        print("2. Gestionar clientes")
        print("3. Gestionar reservas")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            while True:
                print("\n--- Gestionar Destinos ---")
                print("1. Añadir destino")
                print("2. Mostrar destinos")
                print("3. Volver al menú principal")

                opcion_destino = input("\nSeleccione una opción: ")

                if opcion_destino == '1':
                    gestionar.añadir_destino()
                elif opcion_destino == '2':
                    gestionar.mostrar_destinos()
                elif opcion_destino == '3':
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")

        elif opcion == '2':
            while True:
                print("\n--- Gestionar Clientes ---")
                print("1. Añadir cliente")
                print("2. Mostrar clientes")
                print("3. Volver al menú principal")

                opcion_cliente = input("\nSeleccione una opción: ")

                if opcion_cliente == '1':
                    gestionar.añadir_cliente()
                elif opcion_cliente == '2':
                    gestionar.mostrar_clientes()
                elif opcion_cliente == '3':
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")

        elif opcion == '3':
            while True:
                print("\n--- Gestionar Reservas ---")
                print("1. Realizar reserva")
                print("2. Cancelar reserva")
                print("3. Mostrar reservas")
                print("4. Volver al menú principal")

                opcion_reserva = input("\nSeleccione una opción: ")

                if opcion_reserva == '1':
                    reservas.realizar_reserva()
                elif opcion_reserva == '2':
                    reservas.cancelar_reserva()
                elif opcion_reserva == '3':
                    reservas.mostrar_reservas()
                elif opcion_reserva == '4':
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")

        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
