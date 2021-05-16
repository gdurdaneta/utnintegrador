from Logicapy import Logica
from modelobd import OperacionesBaseDatos


class Inicio (Logica):
    
    
  def iniciar(self):
      Logica.login(self)
      OperacionesBaseDatos.crearbaseytabla


Inicio().iniciar()