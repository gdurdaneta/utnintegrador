from Main_Windows_base import Ui_MainWindow
from funcionescnclase import (buscardatos, ingresarusuario,borrar)

class Logica():

    def __init__(self):
        self.lista = []

    def guardardatos(self, Entry_Apellido, Entry_Nombre, Entry_DNI, Entry_Sexo, Entry_Telefono, Entry_Usuario, Entry_Password):
        self.lista.append = [Entry_Apellido, Entry_Nombre, Entry_DNI, Entry_Sexo, Entry_Telefono, Entry_Usuario, Entry_Password]

    def ingresousuario(self, Entry_Usuario, Entry_Password):
        pass
        