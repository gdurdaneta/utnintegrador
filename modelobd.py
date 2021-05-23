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
        
        print("\n Se ha creado el usuario.\n")

    def borrar(self, usuario, password):
        """
        Metodo para el borrado de usuarios previa coincidencia de usuario y password.
        """
        
        try:
            print(usuario, password)
            self.dbcursor.execute("DELETE FROM integrador WHERE Usuario =? and Password =?",(usuario, password,))
            self.db.commit()
            self.db.close()
            print(self.dbcursor.rowcount)
            print("Borrado exitoso.")
        except:
            ("Convinacion de usuario y contraseña invalido.")

    def ingresousuarios(self, usuario, password):
        """
        Metodo que consulta en la base de datos una coincidencia unica de usuario y password.
        """
        try:
            self.dbcursor.execute("SELECT nombre FROM integrador WHERE Usuario=? AND Password =?", (usuario, password))
            self.db.commit()
            busqueda = self.dbcursor.fetchone()
            print((busqueda))
            if busqueda is not None:
                print("Haz ingresado a la base de datos.")
                self.dbcursor.close()
                return True
            else:
                print("hello mundo abajo false")
        except Exception as e:
            print(e)

   
    def consultageneral(self, usuario):
        """
        Metodo que busca una coincidendia de usuario en la base de datos.
        """
        try:
            self.dbcursor.execute("SELECT * FROM integrador WHERE Usuario=?", (usuario,))
            tabla = self.dbcursor.fetchone()
            for datos in tabla:
                self.consulta.append(datos)
            self.dbcursor.close()
            return self.consulta
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)

    def modificarusuario (self, dato, datoNuevo, usuario):
<<<<<<< HEAD
            try:
                self.dbcursor.execute(f"UPDATE integrador SET {dato}='{datoNuevo}' where Usuario='{usuario}'")
                self.dbcursor.execute(f"SELECT * FROM integrador")
                self.db.commit()
                print(type(usuario))
                busqueda = self.dbcursor.fetchall()
                for datos in busqueda:
                    print(datos)
            
            except Exception as e:
                print(e)
=======
        """
        Metodo para modificar datos de usuarios a traves de los entry en codigo de visual2.py.
        """
        try:
            print("dato ", str(dato))
            print("Dato nuevo " , str(datoNuevo))
            print("usuario " , str(usuario))
            print(f"UPDATE integrador SET {dato} VALUES {datoNuevo} WHERE Usuario={usuario}")
            print("antes de update ")
            self.dbcursor.execute(f'UPDATE integrador SET {dato} = {datoNuevo} WHERE Usuario = {usuario}')
            print("Desúes de update")
            self.db.commit()
            busqueda = self.dbcursor.fetchone()
            print(busqueda)
        
        except Exception as e:
            print(e)
>>>>>>> 039b61dcf140015bfa9a9a89a879e1d7e8bc52bc

