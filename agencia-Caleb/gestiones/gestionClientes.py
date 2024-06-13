clientes = []

def anadirCliente(idCliente, nombre):
    cliente = {'id_cliente': idCliente, 'nombre': nombre}
    clientes.append(cliente)
    print(f'Cliente {nombre} añadido.')

def clienteExiste(idCliente):
    for cliente in clientes:
        if cliente['id_cliente'] == idCliente:
            return True
    return False

def mostrarClientes():
    print('Clientes:')
    for cliente in clientes:
        print(f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']}")

def obtenerNombreCliente(idCliente):
    for cliente in clientes:
        if cliente['id_cliente'] == idCliente:
            return cliente['nombre']
    return None
