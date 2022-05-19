import tkinter as tk
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import filedialog


class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):

        super().__init__()

        self.controller = controller

        self.title("NeuroFiler 0.1")
        self._create_widgets()

    #
    def main(self):
        self.mainloop()

    # Crea varios widgets en la ventana principal

    def _create_widgets(self):
        # Crea el frame
        self.window = tk.Frame(self)
        # Le da un tamaño al frame
        self.geometry("1200x720")
        # Crea la cinta de opciones
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_cascade(label="Abrir", command=self.load_file)
        file_menu.add_cascade(label="Exit", command=quit)

    def load_file(self):
        self.controller.load_file()
