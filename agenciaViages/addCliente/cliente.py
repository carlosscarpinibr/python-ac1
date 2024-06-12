# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def añadir_cliente():
    """
    Solicita al usuario los datos de un nuevo cliente y lo añade a la lista de clientes.

    Parámetros:
    None

    Retorno:
    None
    """
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = {'id': id_cliente, 'nombre': nombre_cliente}
    clientes.append(cliente)
    print(f"Cliente añadido: {id_cliente} - {nombre_cliente}")