from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        # La interfaz pide un argumento de controller para funcionar
        self.view = View(self)

    def main(self):
        # llama a la interfaz grafica
        self.view.main()
        print('Hola mundo desde el controller')


if __name__ == '__main__':
    # Cuando creamos una instancia de controller llamamos a model y view
    programa = Controller()
    # despues llamamos al metodo principal de controller y loopeamos la interfaz
    programa.main()
