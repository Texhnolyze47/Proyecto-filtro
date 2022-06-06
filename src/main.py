# This is a sample Python script.
from tkinter import filedialog

from src.conexion import conexion
from src.ports import *
import pandas as pd
import matplotlib.pyplot as plt
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
    fig = graficador_searborn()

    canvas = FigureCanvasTkAgg(fig, master=nueva_ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()


def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='c:/',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
    archivoRuta.append(archivo)
    ventana_graficos()



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
    nuevosDatos = datos[
        ['Nodo1', 'Nodo2', 'Nodo3', 'Nodo4', 'Nodo5', 'Nodo6', 'Nodo7', 'Nodo8', 'Nodo9', 'Nodo10', 'Nodo11', 'Nodo12',
         'Nodo13', 'Nodo14']]

    fig = plt.figure()
    plt.plot(nuevosDatos)
    return fig


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




if __name__ == '__main__':

    conexion()

    ventana_boton()
    ventana_graficos()
