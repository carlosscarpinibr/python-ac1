# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def obtener_cliente(id_cliente):
    for client in clientes:
        if client['id'] == id_cliente:
            return client
    return False