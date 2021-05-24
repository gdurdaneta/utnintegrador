from typing import get_args
from Logicapy import *
from sqlite3.dbapi2 import Cursor, connect
import sqlite3

class OperacionDB():
    """
    Clase para la operaciones de la base de datos.
    """
    def __init__(self):
        """
        Se establece la conexion con la base de datos y el cursor. Se establece variable consulta.
        """
        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        self.consulta = []

    def crearbaseytabla(self):
        """
        Funcion que crea la base de datos y la tabla integrador.
        """
        try:
            self.dbcursor.execute('''CREATE TABLE integrador (Usuario VARCHAR(10) NOT NULL UNIQUE, 
                                                            Password VARCHAR(10) NOT NULL, 
                                                            Nombre VARCHAR(20) NOT NULL, 
                                                            Apellido VARCHAR(20) NOT NULL, 
                                                            Dni INTENGER(10) NOT NULL, 
                                                            Telefono INTEGER(10) NOT NULL)''')
            self.db.commit()
            self.db.close()
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
        finally:
            print("Base de datos conectada Correctamente")

    def creausuario(self, lista):
        """
        Metodo para la generacion de nuevos usuarios en la base de datos.
        """
        sql = """INSERT INTO integrador (Usuario, 
                                        Password, 
                                        Nombre, 
                                        Apellido,  
                                        Dni, 
                                        Telefono) 
                                        VALUES (?, ?, ?, ?, ? ,?)"""
        self.db.execute(sql, lista)
        self.db.commit()
        self.db.close()
        
    def borrar(self, usuario, password):
        """
        Metodo para el borrado de usuarios previa coincidencia de usuario y password.
        """
        self.dbcursor.execute("DELETE FROM integrador WHERE Usuario =? and Password =?",(usuario, password,))
        self.db.commit()
        self.db.close()
        print(self.dbcursor.rowcount)

    def ingresousuarios(self, usuario, password):
        """
        Metodo que consulta en la base de datos una coincidencia unica de usuario y password.
        """
        self.dbcursor.execute("SELECT nombre FROM integrador WHERE Usuario=? AND Password =?", (usuario, password))
        self.db.commit()
        busqueda = self.dbcursor.fetchone()
        if busqueda is not None:
            self.dbcursor.close()
            return True

    def consultageneral(self, usuario):
        """
        Metodo que busca una coincidendia de usuario en la base de datos.
        """
        self.dbcursor.execute("SELECT * FROM integrador WHERE Usuario=?", (usuario,))
        tabla = self.dbcursor.fetchone()
        return tabla

    def modificarusuario (self, dato, datoNuevo, usuario):
            
        self.dbcursor.execute(f"UPDATE integrador SET {dato}='{datoNuevo}' where Usuario='{usuario}'")
        self.dbcursor.execute(f"SELECT * FROM integrador")
        self.db.commit()



