def nuevaReserva(tablaDestino, tablaClientes):
        '''
        Descripción: crea una nueva reserva utilizando las informaciones de las lista de destinos y de la lista de clientes.
        Entradas: introducimos el código del destino, que es una cadena de texto y la variable del tipo entero para el ID del cliente.
        Salidas: es de tipo diccionario, haciendo uso de las entradas previamente introducidas y usaremos los valores de nombreCliente, 
        nombreDestino y precioDest para completar.
        '''
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
        '''
        Descripción: cancelamos las reservas realizadas previamente en la lista de reservas.
        Entradas: introducimos el código del destino, que es una cadena de texto y la variable del tipo entero para el ID del cliente.
        Salidas: es una variable del tipo diccionario, con las los datos previamente introducidos, usaremos los valores de nombreCliente, 
        nombreDestino y precioDest para completar. La variable diccionario será utilizada como referencia como referencia para  realizar la cancelación oportuna. 
        '''
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
    '''
    Descripción: mostramos la lista de las reservas del programa principal.
    Entradas: introducimos el la lista de reservas del programa principal.
    Salida: imprimimos la lista de reservas.
    '''
    for entrada in tabla:
        print(f'Reserva de {entrada['nombreCliente']}, destino: {entrada['nombreDestino']}({entrada['codigoDestino']}) por {entrada['precioDest']} €.')
