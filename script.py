import os

def limpiar_pantalla():
    os.system('clear') #clear screen mac
    #os.system('cls') #clear screen windows
    
def pausar_pantalla():
    print('Pulse Enter para continuar... ')
    input()


def nuevoDestino():
    codDest = input('Entra el codigo del destino: ')
    nomDest = input('Entra el nombre del destino: ')
    precDest = input('Entra el precio del destino: ')
    
    destino = {'codigoDest' : codDest , 'nombreDest' : nomDest , 'precioDest' : precDest}
    
    return destino

def mostrar_destinos(tabla):
    for entrada in tabla:
        print(f'Código: {entrada['codigoDest']} - Nombre: {entrada['nombreDest']} - Precio: {entrada['precioDest']} €')


def nuevoCliente():
    idCli = input('Entre un ID para el cliente: ')
    nomCli = input('Entre el nombre del cliente: ')
    
    cliente = {'idCliente' : idCli , 'nombreCli' : nomCli}
    
    return cliente

def mostrar_clientes(tabla):
    for entrada in tabla:
        print(f'ID: {entrada['idCliente']} - Nombre: {entrada['nombreCli']}')

def nuevaReserva(tablaDestino, tablaClientes):
        entraCod = input('Entra el código del destino: ')
        entraId = input('Entra la ID del cliente: ')
        flag1 = False
        flag2 = False
        for entradaDest in tablaDestino:
            if entraCod == entradaDest['codigoDest']:
                flag1 = True
                entraDest = entradaDest['nombreDest']
        for entradaId in tablaClientes:
            if entraId == entradaId['idCliente']:
                flag2 = True
                entraCli = entradaId['nombreCli']
        if flag1 and flag2 == True:
            reserva = {'codigoDestino' : entraCod , 'idCliente' : entraId , 'nombreCliente' : entraCli , 'nombreDestino' : entraDest}
            return True, reserva
        else:
            return False, None

def cancelaReserva(tabla):
        entraCod = input('Entra el código del destino: ')
        entraId = input('Entra la ID del cliente: ')
        flag1 = False
        flag2 = False
        j = 0
        for entradaCod in tabla:
            if entraCod == entradaCod['codigoDestino']:
                flag1 = True
                entraDest = entradaCod['nombreDestino']
        for entradaId in tabla:
            if entraId == entradaId['idCliente']:
                flag2 = True
                entraCli = entradaId['nombreCliente']
        if flag1 and flag2 == True:
            cancela = {'codigoDestino' : entraCod , 'idCliente' : entraId , 'nombreCliente' : entraCli , 'nombreDestino' : entraDest}
            return True, cancela
        else:
            return False, None                

def mostrar_reservas(tabla):
    for entrada in tabla:
        print(f'ID: {entrada['idCliente']} - Nombre: {entrada['nombreCliente']} - Destino: {entrada['codigoDestino']} - {entrada['nombreDestino']} ')




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
        #limpiar_pantalla()
        if menu == '1':
            print('Añadir un nuevo destino')
            tablaDestinos.append(nuevoDestino())
            print('Destino añadido corectamente.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '2':
            print('Añadir un nuevo cliente')
            tablaClientes.append(nuevoCliente())
            print('Cliente añadido corectamente.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '3':
            print('Realizar una reserva')
            verifica3, nuevaReserv = nuevaReserva(tablaDestinos, tablaClientes)
            if verifica3 == True:
                tablaReservas.append(nuevaReserv)
                print('Reserva añadida corectamente.')
            else:
                print('El codigo de destino o ID del usuario no existe, intente nuevamente.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '4':
            print('Cancelar una reserva')
            verifica4, cancela = cancelaReserva(tablaReservas)
            if verifica4 == True:
                #print(marcador4)
                tablaReservas.remove(cancela)
                print('La reserva fue cancelada.')
            else:
                print('El codigo de destino o ID del usuario no existe, intente nuevamente.')  
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '5':
            print('Mostrar todos los destinos')
            mostrar_destinos(tablaDestinos)
            pausar_pantalla()
            #limpiar_pantalla()
        elif menu == '6':
            print('Mostrar todos los clientes')
            mostrar_clientes(tablaClientes)
            pausar_pantalla()
            #limpiar_pantalla()
        elif menu == '7':
            print('Mostrar todas las reservas')
            mostrar_reservas(tablaReservas)
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '0':
            print('Fin del programa')
        else:
            print('Opción inválida, intente nuevamente.')
            pausar_pantalla()
            limpiar_pantalla()

#Llama principal()
principal()