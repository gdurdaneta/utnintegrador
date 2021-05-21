from typing import get_args
from Logicapy import *
from sqlite3.dbapi2 import Cursor, connect
#from Logicapy import Logica
import sqlite3

class OperacionDB():

    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        self.consulta = []

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

    def creausuario(self, lista):

        sql = """INSERT INTO integrador (Usuario, 
                                        Password, 
                                        Nombre, 
                                        Apellido,  
                                        Dni, 
                                        Telefono) 
                                        VALUES (?, ?, ?, ?, ? ,?)"""
        #self.db.cursor.execute(sql, args) 
        #self.dbcursor.execute(sql, args)
        self.db.execute(sql, lista)
        self.db.commit()
        
        self.db.close()
        
        print("\n Se ha creado el usuario.\n")

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

    def borrartodo(self):
        ordenborrartodo = input("¿Seguro que quiere borrar todo? S/N: \n")
        if ordenborrartodo == "S" or ordenborrartodo == "s":        
            self.conexion(self.db, self.dbcursor)
            self.dbcursor.execute("DROP TABLE usuarios")
            self.db.close()
            print("Base de datos eliminada.")
        elif ordenborrartodo == "N" or ordenborrartodo == "n":
            print("La base de datos no se elimino.")
        else:
            print("Ingreso invalido.")

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
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
        
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

    def modificarusuario (self, dato, datoNuevo, usuario):

            try:
                print(dato)
                print(datoNuevo)
                
                print(f"UPDATE integrador SET {dato} VALUES {datoNuevo} WHERE Usuario={usuario}")
                # print("Buscando ... ")
                # print("Encontre ")
                
                # print("Actualizando por " + usuario)
                print("antes de update ")
                self.dbcursor.execute(f"UPDATE integrador SET {str(dato)}={str(datoNuevo)} WHERE Usuario={str(usuario)}")
                #self.dbcursor.execute("UPDATE integrador SET Password=fran WHERE Usuario=fran")
                #self.dbcursor.execute("UPDATE integrador SET Password VALUES frab WHERE Usuario=fran")
                print("Desúes de update")
                print(sqlite3.OperationalError)
                self.dbcursor.execute(f"SELECT {dato} FROM integrador WHERE Usuario={usuario}")
                self.db.commit()
                busqueda = self.dbcursor.fetchone()
                print(busqueda)
            
            except sqlite3.OperationalError:
                print(sqlite3.OperationalError)
                print("Ingrese una convinación valida.")
                pass

