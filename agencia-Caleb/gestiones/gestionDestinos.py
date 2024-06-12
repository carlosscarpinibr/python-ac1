# gestion_destinos.py

destinos = []

# Función para añadir un nuevo destino
def anadirDestino(codigo, nombre, precio):
    destino = {'codigo': codigo, 'nombre': nombre, 'precio': precio}
    destinos.append(destino)
    print(f'Destino {nombre} añadido.')

# Función para comprobar si un destino existe
def destinoExiste(codigoDestino):
    for destino in destinos:
        if destino['codigo'] == codigoDestino:
            return True
    return False

# Función para obtener el nombre del destino
def obtenerNombreDestino(codigoDestino):
    for destino in destinos:
        if destino['codigo'] == codigoDestino:
            return destino['nombre']
    return None

# Función para mostrar todos los destinos
def mostrarDestinos():
    print('Destinos:')
    for destino in destinos:
        print(f"Código: {destino['codigo']}, Nombre: {destino['nombre']}, Precio: {destino['precio']}")

