import sys 
from modelobd import OperacionDB



class logica():
    def __init__(self):
        pass
        #datos = mainlogin
        #self.usuario = datos().Entry_Usuario
        #self.password = datos().Entry_Password
        

    def botoningreso(self,username,password) :
        try:
            OperacionesBaseDatos().ingresousuarios(username, 
                                                   password)
            print(OperacionesBaseDatos().ingresousuarios(username, 
                                                   password))                                       
        except:
            print("operaciones base de datos en logica ")
            pass #Pantalla de alerta
        finally:
            pass
        #Alerta de ingreso valido y luego a crear ???

    def botoncrear():
        try:
            OperacionesBaseDatos().creausuario() #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botonconsultar():
        try:
            OperacionesBaseDatos().consultageneral() #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botonmodificar():
        try:
            OperacionesBaseDatos().modificarusuario() #No entiendo como se utlizan estos args
        except:
            pass #Pantalla de alerta
        finally:
            pass

    def botoneliminar(self):
        try:
            OperacionesBaseDatos().borrar(self.usuario,
                                        self.password) 
        except:
            pass #Pantalla de alerta
        finally:
            pass


