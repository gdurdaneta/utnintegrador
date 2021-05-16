from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys


from Main_Windows_logins import mainlogin
from Main_Windows_base import mainbase
from Error_Usuario_Inexistente import usuario_inexistente
from error_password_incorrecto import contraseña_incorrecta
"from logicapy import validauser"
"from BD_models import buscarusuario"
"from BD_models import buscarpassword"

class integrador(QtWidgets.QMainWindow):
    def __init__(self):
        super(integrador, self).__init__()
        self.ui = mainlogin()
        self.ui.setupUi(self)

            

app = QtWidgets.QApplication([])
aplicacion = integrador()
aplicacion.show()
sys.exit(app.exec())
