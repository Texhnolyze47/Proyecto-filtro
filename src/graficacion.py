import pandas as pd
from matplotlib import pyplot as plt

from src.main import archivoRuta


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