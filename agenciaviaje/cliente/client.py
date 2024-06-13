def nuevoCliente():
    '''
    Descripcion: función para crear un nuevo cliente.
    Entrada de datos: una variable entera para el ID del cliente
      y un cadena de texto para el nombre del cliente.
    Salida de datos: una variable del tipo diccionario, con los datos ingresados previamente.
    '''
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
    '''
    Descripcion: la función coteja los datos ingresados y los muestra en pantalla.
    Entrada de datos: la lista de clientes del programa principal.
    Salida de datos: mostramos la informacion de la lista por pantalla.
    '''
    for entrada in tabla:
        print(f'ID: {entrada['idCliente']} - Nombre: {entrada['nombreCli']}')
