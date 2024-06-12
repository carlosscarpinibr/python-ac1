# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def anadir_destino():
    """
    Solicita al usuario los datos de un nuevo destino y lo añade a la lista de destinos.

    Parámetros:
    None

    Retorno:
    None
    """
    codigo = input("Ingrese el código del destino: ")
    nombre = input("Ingrese el nombre del destino: ")
    try:
        precio = float(input("Ingrese el precio del destino: "))
        destino = {'codigo': codigo, 'nombre': nombre, 'precio': precio}
        destinos.append(destino)
        print(f"Destino añadido: {codigo} - {nombre} - {precio:.2f}€")
    except ValueError:
        print("El precio debe ser un número válido.")