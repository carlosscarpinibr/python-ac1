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
