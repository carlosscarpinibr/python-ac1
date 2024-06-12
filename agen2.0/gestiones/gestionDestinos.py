destinos = []

def anadirDestino(codigo, nombre, precio):
    destino = {'codigo': codigo, 'nombre': nombre, 'precio': precio}
    destinos.append(destino)
    print(f'Destino {nombre} añadido.')

def destinoExiste(codigoDestino):
    for destino in destinos:
        if destino['codigo'] == codigoDestino:
            return True
    return False

def mostrarDestinos():
    print('Destinos:')
    for destino in destinos:
        print(f"Código: {destino['codigo']}, Nombre: {destino['nombre']}, Precio: {destino['precio']}")

def obtenerNombreDestino(codigoDestino):
    for destino in destinos:
        if destino['codigo'] == codigoDestino:
            return destino['nombre']
    return None
