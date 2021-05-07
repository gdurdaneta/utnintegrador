from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

from Main_Windows_logins import mainlogin
from Main_Windows_base import mainbase
"from logicapy import validauser"
"from BD_models import buscarusuario"
"from BD_models import buscarpassword"

class integrador(QtWidgets.QMainWindow):
    def __init__(self):
        super(integrador, self).__init__()
        self.ui = mainlogin()
        self.ui.setupUi(self)

    def validador(self):
        if buscarusuario == Entry_Usuario:
            if buscarpassword == Entry_Password:
                Main_Windows_base()
            else:
                print("password incorrecto")
        else:
            print("Usuario Incorrecto")
            

app = QtWidgets.QApplication([])
aplicacion = integrador()
aplicacion.show()
sys.exit(app.exec())
