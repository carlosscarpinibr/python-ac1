import os
from agenciaviaje.destino.destination import nuevoDestino
from agenciaviaje.destino.destination import mostrar_destinos
from agenciaviaje.cliente.client import nuevoCliente
from agenciaviaje.cliente.client import mostrar_clientes
from agenciaviaje.reserva.reservation import nuevaReserva
from agenciaviaje.reserva.reservation import cancelaReserva
from agenciaviaje.reserva.reservation import mostrar_reservas



def limpiar_pantalla():
    #os.system('clear') #clear screen mac
    os.system('cls') #clear screen windows
    
def pausar_pantalla():
    print('Pulse Enter para continuar... ')
    input()

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