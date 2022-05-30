# This is a sample Python script.
from tkinter import filedialog

import pandas as pd
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
from tkinter import *

archivoRuta = []


def ventana_graficos():
    nueva_ventana = Tk()
    ventana.destroy()
    # Le da nombre a la segunda ventana
    nueva_ventana.title("NeuralFilter")

    nueva_ventana.geometry("1280x720")





def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='c:/',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
    archivoRuta.append(archivo)
    print(archivo)
    ventana_graficos()


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


# funcion que grafica


def graficador_matploy():
    datos = pd.read_excel(abrir_archivo()).head()

    # variable que va a graficar

    x1 = list(datos['nodo1'])
    x2 = list(datos['nodo2'])
    x3 = list(datos['nodo3'])
    x4 = list(datos['nodo4'])
    x5 = list(datos['nodo5'])
    x6 = list(datos['nodo6'])
    x7 = list(datos['nodo7'])
    x8 = list(datos['nodo8'])
    x9 = list(datos['nodo9'])
    x10 = list(datos['nodo10'])
    x11 = list(datos['nodo11'])
    x12 = list(datos['nodo12'])
    x13 = list(datos['nodo13'])
    x14 = list(datos['nodo14'])
    # layout
    figure, axis = plt.subplots(5, 3)
    # posiciones y data a graficar
    axis[0, 0].plot(x1)
    axis[0, 0].set_title('nodo 1')

    axis[0, 1].plot(x2)
    axis[0, 1].set_title('nodo 2')

    axis[0, 2].plot(x3)
    axis[0, 2].set_title('nodo 3')

    axis[1, 0].plot(x4)
    axis[1, 0].set_title('nodo 4')

    axis[1, 1].plot(x5)
    axis[1, 1].set_title('nodo 5')

    axis[1, 2].plot(x6)
    axis[1, 2].set_title('nodo 6')

    axis[2, 0].plot(x7)
    axis[2, 0].set_title('nodo 7')

    axis[2, 1].plot(x8)
    axis[2, 1].set_title('nodo 8')

    axis[2, 2].plot(x9)
    axis[2, 2].set_title('nodo 9')

    axis[3, 0].plot(x10)
    axis[3, 0].set_title('nodo 10')

    axis[3, 1].plot(x11)
    axis[3, 1].set_title('nodo 11')

    axis[3, 2].plot(x12)
    axis[3, 2].set_title('nodo 12')

    axis[4, 0].plot(x13)
    axis[4, 0].set_title('nodo 13')

    axis[4, 1].plot(x14)
    axis[4, 1].set_title('nodo 14')

    plt.show()





def encode_send(ard, data):
    # print(f"enviar: {data}")
    enc = f"{data}\n".encode("UTF-8")
    print(f"enviar: {data}")

    ard.write(enc)


def decode_response(ard):
    linea = ard.readline()
    respuesta = linea.decode()
    print("Tipo de variable", linea)
    print("Tipo de variable", respuesta)
    return respuesta


def conexion():
    try:
        ser = serial.Serial(port_arduino, 9600, timeout=1)
        print('Arduino conectado', port_arduino)
        print('Conexion Hecha')
    except:
        print("La conexion fallo")


if __name__ == '__main__':
    # objecto con la info de la conexion de arduino
    portsEncontrados = get_ports()
    # variable con el puerto que va utlizar arduino para conectarse con la pc
    port_arduino = conectar_arduino(portsEncontrados)

    # creamos la ventana
    ventana = Tk()
    # le damos nombre de la ventanna
    ventana.title("Abrir archivo")
    # le damos un tamaño a la ventana
    ventana.geometry("1280x720")
    # Establecer el grosor de la fila
    # y la columna en la que se encuentra el widget
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)

    contenedor = Frame(ventana)
    # Establecer el grosor de la columna
    contenedor.grid(row=0, column=0)

    # Creamos un boton
    abrir_boton = Button(contenedor, text="Abrir Archivo", command=abrir_archivo, width=15, height=5)
    abrir_boton.grid(pady=10, padx=20)

    conexion()

    ventana.mainloop()

