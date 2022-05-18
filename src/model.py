from tkinter import filedialog
import pandas as pd


class Model:

    def __init__(self):
        '''
        Constructor
        '''

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(initialdir='c:/', title='Seleccione archivo',
                                             filetype=(('xlsx files', '*.xlsx'), ('All files', '*.*')))
        pd.read_excel(archivo).head()

        return pd
