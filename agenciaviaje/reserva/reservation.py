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
