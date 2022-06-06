# This is a sample Python script.
from tkinter import filedialog

import pandas as pd
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

# ruta del archivo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotly.graph_objs import Figure

archivoRuta = []

# creamos la ventana
ventana = Tk()


def ventana_boton():
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

    ventana.mainloop()


def ventana_graficos():
    nueva_ventana = Tk()
    ventana.destroy()
    # Le da nombre a la segunda ventana
    nueva_ventana.title("NeuralFilter")

    nueva_ventana.geometry("1280x720")
    graficador_searborn()


def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='c:/',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
    archivoRuta.append(archivo)
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
    print("Entro al graficador")

    ruta = ""
    # datos = pd.read_excel(ruta.join(archivoRuta))

    df = pd.read_excel(ruta.join(archivoRuta))

    # ax = column.plot.line(x="Nodos", y="seconds")
    plt.show()


def graficador_searborn():
    print("Entro al graficador")

    ruta = ""
    datos = pd.read_excel(ruta.join(archivoRuta))
    nuevosDatos = datos[['Nodo1','Nodo2','Nodo3','Nodo4','Nodo5','Nodo6','Nodo7','Nodo8','Nodo9','Nodo10','Nodo11','Nodo12',
    'Nodo13','Nodo14']]

    nuevosDatos.plot()
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

    conexion()

    ventana_boton()
    ventana_graficos()
