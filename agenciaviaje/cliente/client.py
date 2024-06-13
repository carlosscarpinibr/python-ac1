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
