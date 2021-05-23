from typing import get_args
from Logicapy import *
from sqlite3.dbapi2 import Cursor, connect
import sqlite3

#Clase para la operaciones de la base de datos.

class OperacionDB():

    #Se establece la conexion con la base de datos y el cursor. Se establece variable consulta.

    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        self.consulta = []

    #Funcion que crea la base de datos y la tabla integrador.

    def crearbaseytabla(self):
        try:
            self.dbcursor.execute('''CREATE TABLE integrador (Usuario VARCHAR(10) NOT NULL, 
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

    #Funcion para la creacion de usuarios.

    def creausuario(self, lista):

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

    #Funcion para el borrado de usuarios donde coiincide usuario y password.

    def borrar(self, usuario, password):
        
        try:
            print(usuario, password)
            self.dbcursor.execute("DELETE FROM integrador WHERE Usuario =? and Password =?",(usuario, password,))
            self.db.commit()
            self.db.close()
            print(self.dbcursor.rowcount)
            print("Borrado exitoso.")
        except:
            ("Convinacion de usuario y contraseña invalido.")

    #Funcion que consulta en la base de datos coincidencia de usuario y password.

    def ingresousuarios(self, usuario, password):
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

    #Funcion de consulta donde busca coinsidencia de usuario.
        
    def consultageneral(self, usuario):
        
        try:
            self.dbcursor.execute("SELECT * FROM integrador WHERE Usuario=?", (usuario,))
            tabla = self.dbcursor.fetchone()
            for datos in tabla:
                self.consulta.append(datos)
            self.dbcursor.close()
            return self.consulta
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)

    #Funcion para la modificacion de usuarios a travez de entrys en codigo de visual2.py.

    def modificarusuario (self, dato, datoNuevo, usuario):

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

