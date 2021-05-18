from PyQt5 import QtWidgets
import sys 
from Main_Windows_logins import mainlogin
from Main_Windows_base import mainbase
from modelobd import OperacionesBaseDatos


class logica():
    def __init__(self):
        datos = mainlogin
        self.usuario = datos().Entry_Usuario
        self.password = datos().Entry_Password
        

    def botoningreso(self) :
        try:
            OperacionesBaseDatos().ingresousuarios(self.usuario, 
                                                   self.password)
        except:
            pass #Pantalla de alerta
        finally:
            pass
        #Alerta de ingreso valido y luego a crear ???

    def botoncrear():
        pass

    def botonconsultar():
        pass

    def botonmodificar():
        pass

    def botoneliminar():
        pass

logica().botoningreso("demo","demo")