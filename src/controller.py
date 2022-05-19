from tkinter import filedialog

import serial
import serial.tools.list_ports

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        # La interfaz pide un argumento de controller para funcionar
        self.view = View(self)

    def main(self):
        # llama a la interfaz grafica
        self.establishes_arduino()
        self.view.main()


    def load_file(self):
        # llama a la funcion abrir archivo en model
        self.model.open_file()

    def establishes_arduino(self):
        ports = self.model.get_port()
        port_arduino = self.model.conect_arduino(ports)

        try:
            ard = serial.Serial(port_arduino,9600, timeout=1)
            print("Arduino conectado", port_arduino)
        except:
            print("La conexcion fallo");



if __name__ == '__main__':
    # Cuando creamos una instancia de controller llamamos a model y view
    programa = Controller()
    # despues llamamos al metodo principal de controller y loopeamos la interfaz
    programa.main()
