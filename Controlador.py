from Logicapy import Logica
from modelobd import OperacionesBaseDatos


class Inicio (Logica):

  def iniciar():
      Logica.login
      OperacionesBaseDatos.crearbaseytabla

Inicio().iniciar()



