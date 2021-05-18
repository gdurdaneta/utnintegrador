import sys 
from modelobd import OperacionesBaseDatos
from visual import loginApp


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
        try:
            OperacionesBaseDatos().creausuario(*args=) #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botonconsultar():
        try:
            OperacionesBaseDatos().consultageneral(*args=) #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botonmodificar():
        try:
            OperacionesBaseDatos().modificarusuario(*args=) #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botoneliminar():
        try:
            OperacionesBaseDatos().borrar(self.usuario,
                                            self.password) 
        except:
            pass #Pantalla de alerta
        finally:
            pass


logica().botoningreso("demo","demo")