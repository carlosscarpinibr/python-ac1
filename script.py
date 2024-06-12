def nuevoDestino():
    codDest = input('Entra el codigo del destino: ')
    nomDest = input('Entra el nombre del destino: ')
    precDest = input('Entra el precio del destino: ')
    
    destino = {'codigoDest' : codDest , 'nombreDest' : nomDest , 'precioDest' : precDest}
    
    return destino

def principal():
    prompt = '''    
                    Menu - Agencia de viajes
                    
                1. Añadir un nuevo destino
                2. Añadir un nuevo cliente
                3. Realizar una reserva
                4. Cancelar una reserva
                5. Mostrar todos los destinos
                6. Mostrar todos los clientes
                7. Mostrar todas las reservas
                0. Salir
            '''
    
    tablaDestinos = []
    tablaClientes = []
    tablaReservas = []
    
    
    menu = 0
    while menu != '0':
        print(prompt)
        menu=input('Entre una opción: ')
        if menu == '1':
            print('Añadir un nuevo destino')
            tablaDestinos.append(nuevoDestino())
        elif menu == '2':
            print('Añadir un nuevo cliente')
        elif menu == '3':
            print('Realizar una reserva')
        elif menu == '4':
            print('Cancelar una reserva')
        elif menu == '5':
            print('Mostrar todos los destinos')
            print(tablaDestinos)
        elif menu == '6':
            print('Mostrar todos los clientes')
        elif menu == '7':
            print('Mostrar todas las reservas')
        elif menu == '0':
            print('Fin del programa')
        else:
            print('Opción inválida, intente nuevamente.')

#Llama principal()
principal()