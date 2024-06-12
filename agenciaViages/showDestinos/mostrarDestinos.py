# Listas para almacenar destinos y clientes
destinos = []
clientes = []
def mostrar_destinos():
    """
    Muestra todos los destinos.

    Parámetros:
    None

    Retorno:
    None
    """
    print("Lista de destinos:")
    for destino in destinos:
        print(f"Código: {destino['codigo']}, Nombre: {destino['nombre']}, Precio: {destino['precio']:.2f}€")