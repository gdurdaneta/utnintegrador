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
        #self.ingreso = False

    def prueba(self):
        sql = "SELECT * FROM integrador"
        self.dbcursor.execute(sql)
        tabla = self.dbcursor.fetchone()
        print(tabla)

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
            sql = "DELETE FROM integrador WHERE usuario =? and password =?",(self.usuario, self.password)
            self.dbcursor.execute(sql)
            self.db.commit()
            self.db.close()
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
        
    def consultageneral(self, *args):
        
        sql = "SELECT * FROM integrador WHERE usuario=?" + args
        try:
            self.dbcursor.execute(sql)
            tabla = self.dbcursor.fetchone()
            for datos in tabla:
                self.consulta.append(datos)
            self.dbcursor.close()
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)

    def modificarusuario (self, *args):

            try:
                self.dbcursor.execute("SELECT %s FROM integrador WHERE Usuario=?}", (args, self.usuario))
                self.db.commit()
                busqueda = self.dbcursor.fetchone()
                print("Buscando ... ")
                print("Encontre ")
                print(busqueda)
                print("Actualizando por " + args)
                sql = "UPDATE integrador SET %s VALUES (%s) WHERE %s=", (args , self.usuario)
                self.db.execute(sql)
                if busqueda is not None:
                    self.dbcursor.execute("UPDATE integrador SET {self.variablemodificar} =? WHERE usuario =? AND password =?", (self.nuevodato,self.usuario,self.password))
                    print("Modificacion realizada con exito.")
                else:
                    print("Convinación de usuario y contraseña incorrecta.")
            
            except sqlite3.OperationalError:
                print(sqlite3.OperationalError)
                print("Ingrese una convinación valida.")


