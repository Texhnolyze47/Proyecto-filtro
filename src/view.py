import tkinter as tk
from tkinter import *
from tkinter import filedialog


class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        '''
     Constructor
     '''
        super().__init__()

        self.controller = controller

        self.title("NeuroFiler 0.1")
        # self._main_frame()
        # self._make_entry()

    def main(self):
        self.mainloop()

    # def _main_frame(self):
    #     self.main_frm = tk.Frame(self)
    #     self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    # def _make_entry(self):
    #     ent = tk.Entry(self.main_frm)
    #     ent.pack()

