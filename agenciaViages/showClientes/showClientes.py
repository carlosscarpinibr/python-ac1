from addDestino.destino import anadir_destino
from addCliente.cliente import añadir_cliente
from showDestinos.mostrarDestinos import mostrar_destinos
# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def mostrar_clientes():
    """
    Muestra todos los clientes.

    Parámetros:
    None

    Retorno:
    None
    """
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}")
    

# Funciones de prueba para demostrar el funcionamiento
if __name__ == "__main__":
    while True:
        print("\n1. Añadir destino")
        print("\n2. Añadir cliente")
        print("\n3. Mostrar destinos")
        print("\n4. Mostrar clientes")
        print("\n5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            ()
        elif opcion == '2':
            añadir_cliente()
        elif opcion == '3':
            mostrar_destinos()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


