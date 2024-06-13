import os
from agenciaviaje.destino.destination import nuevoDestino
from agenciaviaje.destino.destination import mostrar_destinos
from agenciaviaje.cliente.client import nuevoCliente
from agenciaviaje.cliente.client import mostrar_clientes
from agenciaviaje.reserva.reservation import nuevaReserva
from agenciaviaje.reserva.reservation import cancelaReserva
from agenciaviaje.reserva.reservation import mostrar_reservas



<<<<<<< HEAD
def limpiar_pantalla():
    '''Descripcion: Funcion del OS que limpia la informacion de la consola
    '''
    #os.system('clear') #clear screen mac
    os.system('cls') #clear screen windows
    
def pausar_pantalla():
    '''Descripcion: Funcion del OS que genera una pausa en la ejecucion del código
    '''
    print('Pulse Enter para continuar... ')
    input()

def verifica_lista(lista):
    '''Descripcion: Funcion que sirve para verificar si la lista introducida esta vacia
       Entrada: Una lista del programa principal
       Salida: un valor booleano (False o True)
    '''
    if len(lista) == 0:
        return False
    else:
        return True


# Menu principal del programa de una cagencia de viajes está diseñado para gestionar y facilitar el proceso de reserva

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
    
    # Variables de las listas que almacenan destinos, clientes y reservas
    tablaDestinos = []
    tablaClientes = []
    tablaReservas = []
    
    
    
    # Menú que presenta y solicita la informacion de cada uno de los pasos requeridos por el programa para la gestion de la misma
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
                    while True:
                        try:
                            tablaReservas.remove(cancela)
                            print('La reserva fue cancelada.')
                            break
                        except ValueError:
                            print('Reserva no existe, intente nuevamente.')
                            break
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
=======
print('otra cosa')

print('Contribución de Manu al repositorio de Carlos')
>>>>>>> a0a12bed1699902056df90695b408229e2158fdf
