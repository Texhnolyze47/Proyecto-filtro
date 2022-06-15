import unittest
from tkinter import filedialog

from src.main import *
from src.ports import get_ports, conectar_arduino


class TestData(unittest.TestCase):

    def test_conexion(self):
        portsEncontrados = get_ports()

        portDefault = 'COM3'

        port = conectar_arduino(ports_encontrados=portsEncontrados)
        self.assertEqual(port, portDefault)

    def test_rutaArchivo(self):
        ruta = "C:/Users/Ivan/PycharmProjects/pythonProject/data/datos_128hz.xlsx"

        archivo = filedialog.askopenfilename(initialdir='c:/',
                                             title='Seleccione archivo',
                                             filetypes=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
        ruta.join(archivo)

        self.assertEqual(ruta,archivo)
