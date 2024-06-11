print('Hola mundo!!')

print('Teste del ordenador')

print("Esto es una prueba")

print('otra cosa')





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

    while opcion !='8':
        print(promt)
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        codigo = input("Ingrese el código del destino: ")
        nombre = input("Ingrese el nombre del destino: ")
        precio = float(input("Ingrese el precio del destino: "))
        print(codigo, nombre, precio)
        print("Destino añadido con éxito.")
    elif opcion == '2':
        mostrar_destinos()
    elif opcion == '3':
        idCliente = input("Ingrese el ID del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        print("Cliente añadido con éxito.")
    elif opcion == '4':
        mostrar_clientes()
    elif opcion == '5':
        idCliente = input("Ingrese el ID del cliente: ")
        codigo_destino = input("Ingrese el código del destino: ")
        print("Reserva realizada con éxito.")
    elif opcion == '6':
        idCliente = input("Ingrese el ID del cliente: ")
        codigo_destino = input("Ingrese el código del destino: ")
        print("Reserva cancelada con éxito.")
    elif opcion == '7':
        mostrar_reservas()
    elif opcion == '8':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
