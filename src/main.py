# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import serial

import serial.tools.list_ports

# esta funcion simplemente regresa el puerto que usa el arduino para conectarse


def get_ports():
    # esto llama a un objeto con la informacion del arduino
    ports = serial.tools.list_ports.comports()
    print('Objeto', ports)
    # retorna el objecto
    return ports

# esta funcion a va regresar el port que utlizar el arduino
# esta funcion necesita el objeto


def conectar_arduino(ports_encontrados):
    # variable donde se almacena el port
    comm_port = "None"
    # en caso de haya mas de un arduino conectado va a tomar ese numero
    # es el numero de veces que se va a repetir el ciclo
    num_connections = len(ports_encontrados)

    for i in range(0, num_connections):
        # le asignamos otra variable al port
        port = ports_encontrados[i]
        print('port antes de hacer cast a un tipo string', port)
        str_port = str(port)
        print('port despues de hacer cast a un tipo string', str_port)
        if 'Arduino' in str_port:
            # se hace un split para extraer el Com
            split_port = str_port.split(' ')
            print('split del string', split_port)
            # se escoge array que tenga el com en este caso esta en la posicion 0
            comm_port = (split_port[0])
            print(comm_port)
    # returna el COM
    return comm_port


if __name__ == '__main__':

    portsEncontrados = get_ports()
    port_arduino = conectar_arduino(portsEncontrados)

    if port_arduino != 'None':
        ser = serial.Serial(port_arduino, 9600, timeout=1)
        print('Arduino conectado', port_arduino)
        print('Conexion Hecha')
    else:
        print('Arduino no conectado')
