from setuptools import setup

setup(
    name = 'agencia de viajes',
    version = '3.0',
    description = 'Programa que simula una agencia de viajes',
    author= 'Albert Ortiz Munté',
    author_email='aomunte@gmail.com',
    url='https://github.com/Riotplayer',
    packages=['agenciaViajes','agenciaViajes.addCliente','agenciaViajes.addDestino',
    'agenciaViajes.cancelarReserva','agenciaViajes.mostrarReservas',
    'agenciaViajes.obtenerCliente','agenciaViajes.obtenerDestino',
    'agenciaViajes.realizarReserva','agenciaViajes.showClientes','agenciaViajes.showDestinos',
    'agenciaViajes.main','agenciaViajes.setup'],
    scripts=['']
)