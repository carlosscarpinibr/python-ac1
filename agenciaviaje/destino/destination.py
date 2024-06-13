def nuevoDestino():
    '''
    Descripcion: 
    Introduce nuevo destino con codigo, nombre y precio del destino
    
    Entrada de datos: 
    - String para codigo y nombre del destino
    - Float para precio del destino
    Salida de datos:
    - Variable tipo diccionario para la funcion principal, 
      con los datos ingresados anteriormente (codigo, nombre y precio)
    '''
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
    '''
    Descripcion: 
    Presenta por consola los destinos introducidos en la lista de destinos
    Entrada de datos: 
    - Lista de destinos ingresados en el programa principal
    Salida de datos:
    - Presentacion de la lista por consola con la informacion de destinos ingresados
    '''
    for entrada in tabla:
        print(f'Código: {entrada['codigoDest']} - Nombre: {entrada['nombreDest']} - Precio: {entrada['precioDest']} €')
