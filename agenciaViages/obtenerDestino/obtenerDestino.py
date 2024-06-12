# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def obtener_destino(codigo_destino):
    for destino in destinos:
        if destino['codigo'] == codigo_destino:
            return destino
    return False