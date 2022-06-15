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
    # fig2 = graficador_searborn_arduino()

    canvas = FigureCanvasTkAgg(fig, master=nueva_ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()
