import tkinter as tk
from tkinter import *
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.graficacion import *
from src.main import archivoRuta

# creamos la ventana
ventana = Tk()


def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='c:/',
                                         title='Seleccione archivo',
                                         filetypes=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
    archivoRuta.append(archivo)
    ventana_graficos()


def ventana_boton():
    # le damos nombre de la ventanna
    ventana.title("Abrir archivo")
    # le damos un tamaño a la ventana
    ventana.geometry("1280x720")
    # Establecer el grosor de la fila
    # y la columna en la que se encuentra el widget
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)


    # creamos una etiqueta con el nombre del programa
    nombreEt = Label(ventana,text="NeuralFilter", font=('Arial',15),width=600,height=2 ,bg="grey")
    nombreEt.pack(side=TOP)


    # Creamos un boton
    abrir_boton = Button(ventana, text="Abrir Archivo", command=abrir_archivo, width=18, bg="grey", height=5)
    abrir_boton.pack(pady=280, padx=20)

    # creamos una etiqueta con un recordatorio
    nombreRecuerdo = Label(ventana,text="Asegurese de tener conectado su Arduino", font=('Arial',12),width=40,height=2)
    nombreRecuerdo.pack(side=BOTTOM)

    ventana.mainloop()


def ventana_graficos():
    nueva_ventana = Tk()
    ventana.destroy()
    # Le da nombre a la segunda ventana
    nueva_ventana.title("NeuralFilter")

    # creamos una etiqueta con el nombre del programa
    nombreEt = Label(nueva_ventana,text="NeuralFilter", font=('Arial',15),width=600,height=2 ,bg="grey")
    nombreEt.pack(side=TOP)

    nueva_ventana.geometry("1280x720")

    fig = graficador_searborn()
    #fig2 = graficador_searborn_arduino()



    canvas = FigureCanvasTkAgg(fig, master=nueva_ventana)
    canvas.get_tk_widget().pack(side=tk.LEFT)
    #canvas2 = FigureCanvasTkAgg(fig2, master=nueva_ventana)
    #canvas2.get_tk_widget().pack(side=tk.RIGHT)
