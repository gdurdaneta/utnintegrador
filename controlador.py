from Main_Windows_login import mainlogin
from logicapy import validauser
from BD_models import buscarusuario
from BD_models import buscarpassword

class utnintegrador:
    def __init__(self):

    def validador(self):
        if buscarusuario == Entry_Usuario:
            if buscarpassword == Entry_Password:
                Main_Windows_base()
            else:
                print("password incorrecto")
        else:
            print("Usuario Incorrecto")
            