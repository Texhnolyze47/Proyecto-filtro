import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from src.main import archivoRuta
from src.envio_datos import *
from src.conexion import *


def graficador_searborn():
    # variabla para colocar la ruta del archivo
    ruta = ""
    # variable para conseguir la ruta del archivo
    datos = pd.read_excel(ruta.join(archivoRuta))
    nuevosDatos = datos[
        ['Nodo1', 'Nodo2', 'Nodo3', 'Nodo4', 'Nodo5', 'Nodo6', 'Nodo7', 'Nodo8', 'Nodo9', 'Nodo10', 'Nodo11', 'Nodo12',
         'Nodo13', 'Nodo14']]
    fig, axes = plt.subplots(4,4)
    for ax,i in zip(axes.ravel(), nuevosDatos.columns[1:]):
        g = sns.lineplot(x='Nodo1', y = i, ax=ax, data=nuevosDatos)


    fig.suptitle("Sin filtrar")
    fig.tight_layout()
    return fig


def graficador_searborn_arduino():
    print("Entro al graficador")

    ruta = ""
    ard = conexion()

    datos = decode_response(ard)
    df = pd.DataFrame(datos)
    fig = plt.subplots(4,4)
    for i in range(1, 14):
        ax = fig.add_subplot(4, 4, i)
        ax.plot(df)
    ax.set_xlabel("Nodos")
    ax.set_ylabel("Segundos")

    fig.suptitle("Filtrada")
    fig.tight_layout()
    return fig
