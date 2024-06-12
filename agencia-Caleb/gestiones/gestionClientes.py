# gestion_clientes.py

clientes = []

# Función para añadir un nuevo cliente
def anadirCliente(idCliente, nombre):
    cliente = {'id_cliente': idCliente, 'nombre': nombre}
    clientes.append(cliente)
    print(f'Cliente {nombre} añadido.')

# Función para comprobar si un cliente existe
def clienteExiste(idCliente):
    for cliente in clientes:
        if cliente['id_cliente'] == idCliente:
            return True
    return False

# Función para obtener el nombre del cliente
def obtenerNombreCliente(idCliente):
    for cliente in clientes:
        if cliente['id_cliente'] == idCliente:
            return cliente['nombre']
    return None

# Función para mostrar todos los clientes
def mostrarClientes():
    print('Clientes:')
    for cliente in clientes:
        print(f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']}")
