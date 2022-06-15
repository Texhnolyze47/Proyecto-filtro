import serial
from src.ports import *


def conexion():
    try:
        ser = serial.Serial(port_arduino, 9600, timeout=1)
        print('Arduino conectado', port_arduino)
        print('Conexion Hecha')
    except:
        print("La conexion fallo")

    return ser
