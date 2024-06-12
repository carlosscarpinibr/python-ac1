print('Hola mundo!!')

print('Teste del ordenador')

print("Esto es una prueba")

print('otra cosa')




#funcion principal
def principal():

    promt = ''' Menú Agencia de Viajes
    1. Añadir destino
    2. Mostrar destinos
    3. Añadir cliente
    4. Mostrar clientes
    5. Realizar reserva
    6. Cancelar reserva
    7. Mostrar reservas
    8. Salir
    '''

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




# creamos listas
destinos = []
clientes = []
reservas = []

# Nuevo destino
def anadirDestino(codigo, nombre, precio):
    destino = {'codigo': codigo, 'nombre': nombre, 'precio': precio}
    destinos.append(destino)
    print(f'Destino {nombre} añadido.')

# Nuevo cliente
def anadirCliente(idCliente, nombre):
    cliente = {'id_cliente': idCliente, 'nombre': nombre}
    clientes.append(cliente)
    print(f'Cliente {nombre} añadido.')

# Existe destino 
def destinoExiste(codigoDestino):
    for destino in destinos:
        if destino['codigo'] == codigoDestino:
            return True
    return False

# cliente existe
def clienteExiste(idCliente):
    for cliente in clientes:
        if cliente['id_cliente'] == idCliente:
            return True
    return False