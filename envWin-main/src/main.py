import tkinter as tk
from models.model import ModeloDatos
from views.view import Vista
from controllers.controller import Controlador

def principal():
    """Lanzador de la aplicación MVC."""
    raiz = tk.Tk()
    modelo = ModeloDatos()
    vista = Vista(raiz)
    controlador = Controlador(modelo, vista)
    raiz.mainloop()

if __name__ == "__main__":
    principal()