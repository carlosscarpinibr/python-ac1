import os

def limpiar_pantalla():
    os.system('clear') #clear screen mac
    #os.system('cls') #clear screen windows
    
def pausar_pantalla():
    print('Pulse Enter para continuar... ')
    input()


def nuevoDestino():
    while True:
        codDest = input('Entra el codigo del destino: ').upper()
        if codDest == '':
            print('El campo no puede estar vacio, intente nuevamente.')
        else:
            break
    while True:
        nomDest = input('Entra el nombre del destino: ').upper()
        if nomDest == '':
            print('El campo no puede estar vacio, intente nuevamente.')
        else:
            break
    while True:
        try:    
            precDest = float(input('Entra el precio del destino: '))
            break
        except ValueError:
            print('Caractere inválido, intente nuevamente.')
    
    destino = {'codigoDest' : codDest , 'nombreDest' : nomDest , 'precioDest' : precDest}
    
    return destino

def mostrar_destinos(tabla):
    for entrada in tabla:
        print(f'Código: {entrada['codigoDest']} - Nombre: {entrada['nombreDest']} - Precio: {entrada['precioDest']} €')


def nuevoCliente():
    while True:
        try:
            idCli = int(input('Entre un ID para el cliente: '))
            break
        except ValueError:
            print('Caractere inválido, intente nuevamente.')
    while True:       
        nomCli = input('Entre el nombre del cliente: ').upper()
        if nomCli == '':
            print('El campo no puede estar vacio, intente nuevamente.')
        else:
            break
            
    cliente = {'idCliente' : idCli , 'nombreCli' : nomCli}
    
    return cliente

def mostrar_clientes(tabla):
    for entrada in tabla:
        print(f'ID: {entrada['idCliente']} - Nombre: {entrada['nombreCli']}')

def nuevaReserva(tablaDestino, tablaClientes):
        while True:
            entraCod = input('Entra el código del destino: ').upper()
            if entraCod == '':
                print('El campo no puede estar vacio, intente nuevamente.')
            else:
                break
        while True:
            try:    
                entraId = int(input('Entra la ID del cliente: '))
                break
            except ValueError:
                print('Caractere inválido, intente nuevamente.')
        flag1 = False
        flag2 = False
        for entradaDest in tablaDestino:
            if entraCod == entradaDest['codigoDest']:
                flag1 = True
                entraDest = entradaDest['nombreDest']
                entraPrec = entradaDest['precioDest']
        for entradaId in tablaClientes:
            if entraId == entradaId['idCliente']:
                flag2 = True
                entraCli = entradaId['nombreCli']
        if flag1 and flag2 == True:
            reserva = {'codigoDestino' : entraCod , 'idCliente' : entraId , 'nombreCliente' : entraCli , 'nombreDestino' : entraDest , 'precioDest' : entraPrec}
            return True, reserva
        else:
            return False, None

def cancelaReserva(tabla):
        while True:
            entraCod = input('Entra el código del destino: ').upper()
            if entraCod == '':
                print('El campo no puede estar vacio, intente nuevamente.')
            else:
                break
        while True:
            try:    
                entraId = int(input('Entra la ID del cliente: '))
                break
            except ValueError:
                print('Caractere inválido, intente nuevamente.')
        flag1 = False
        flag2 = False
        for entradaCod in tabla:
            if entraCod == entradaCod['codigoDestino']:
                flag1 = True
                entraDest = entradaCod['nombreDestino']
                entraPrec = entradaCod['precioDest']
        for entradaId in tabla:
            if entraId == entradaId['idCliente']:
                flag2 = True
                entraCli = entradaId['nombreCliente']
        if flag1 and flag2 == True:
            cancela = {'codigoDestino' : entraCod , 'idCliente' : entraId , 'nombreCliente' : entraCli , 'nombreDestino' : entraDest , 'precioDest' : entraPrec}
            return True, cancela
        else:
            return False, None                

def mostrar_reservas(tabla):
    for entrada in tabla:
        print(f'Reserva de {entrada['nombreCliente']}, destino: {entrada['nombreDestino']}({entrada['codigoDestino']}) por {entrada['precioDest']} €.')

def verifica_lista(lista):
    if len(lista) == 0:
        return False
    else:
        return True


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
        limpiar_pantalla()
        if menu == '1':
            print('1. Añadir un nuevo destino\n')
            tablaDestinos.append(nuevoDestino())
            print('Destino añadido corectamente.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '2':
            print('2. Añadir un nuevo cliente\n')
            tablaClientes.append(nuevoCliente())
            print('Cliente añadido corectamente.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '3':
            print('3. Realizar una reserva\n')
            if verifica_lista(tablaDestinos) and verifica_lista(tablaClientes)  == True:
                verifica3, nuevaReserv = nuevaReserva(tablaDestinos, tablaClientes)
                if verifica3 == True:
                    tablaReservas.append(nuevaReserv)
                    print('Reserva añadida corectamente.')
                else:
                    print('El codigo del destino o ID del usuario no existe, intente nuevamente.')
            else:
                print('No hay codigo del destino o ID del usuario registrado en el sistema.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '4':
            print('4. Cancelar una reserva\n')
            if verifica_lista(tablaReservas) == True:
                verifica4, cancela = cancelaReserva(tablaReservas)
                if verifica4 == True:
                    tablaReservas.remove(cancela)
                    print('La reserva fue cancelada.')
                else:
                    print('El codigo de destino o ID del usuario no existe, intente nuevamente.')
            else:
               print('La lista está vacía.')   
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '5':
            print('5. Mostrar todos los destinos\n')
            if verifica_lista(tablaDestinos) == True:
                mostrar_destinos(tablaDestinos)
            else:
                print('La lista está vacía.')
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '6':
            print('6. Mostrar todos los clientes\n')
            if verifica_lista(tablaClientes) == True:
                mostrar_clientes(tablaClientes)
            else:
               print('La lista está vacía.') 
            pausar_pantalla()
            limpiar_pantalla()
        elif menu == '7':
            print('7. Mostrar todas las reservas\n')
            if verifica_lista(tablaReservas) == True:
                mostrar_reservas(tablaReservas)
            else:
                print('La lista está vacía.') 
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