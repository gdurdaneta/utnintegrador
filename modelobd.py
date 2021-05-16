from sqlite3.dbapi2 import Cursor
#from Logicapy import Logica
import sqlite3

class OperacionesBaseDatos():

    def __init__(self):

        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        self.contador = 3
        self.consulta = []

    def crearbaseytabla(self):
        try:
            self.dbcursor.execute('''CREATE TABLE integrador (Usuario VARCHAR(10) NOT NULL, 
                                                            Password VARCHAR(10) NOT NULL, 
                                                            Nombre VARCHAR(20) NOT NULL, 
                                                            Apellido VARCHAR(20) NOT NULL, 
                                                            Dni INTENGER(10) NOT NULL, 
                                                            Sexo VARCHAR(10) NOT NULL, 
                                                            Telefono INTEGER(10) NOT NULL)''')
            self.db.commit()
            self.db.close()
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
        finally:
            print("Base de datos conectada Correctamente")

    def creausuarios(self, usuario, nombre, apellido, sexo, telefono, password, dni):

        self.dbcursor.execute(
            "INSERT INTO integrador (Usuario, Password, Nombre, Apellido, Sexo, Telefono, Dni) VALUES (?, ?, ?, ?, ?, ? ,?)",
            (self.usuario, self.password, self.nombre, self.apellido, self.sexo, self.telefono, self.dni))
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

        print("\nMenu de acceso a usuarios:\n")
        #self.conexion(self.db, self.dbcursor)

        while self.contador != 0:
        
            self.usuario = input("Ingrese el usuario: ")
            self.password = input("Ingrese el contraseña: ")

            try:
                self.dbcursor.execute("SELECT nombre FROM integrador WHERE Usuario=? AND Password =?", (self.usuario, self.password))
                self.db.commit()
                busqueda = self.dbcursor.fetchone()
                if busqueda is not None:
                    print("Haz ingresado a la base de datos.")
                    self.db.close()
                else:
                    self.contador -=1
                    print(F"Convinacion de usuario y contraseña invalido.\nLe quedan {self.contador} intentos.")
            
            except sqlite3.OperationalError:
                print(sqlite3.OperationalError)
                self.contador -=1
                print(F"Ingrese un usuario y password valido.\nLe quedan {self.contador} intentos.")
                
        if self.contador == 0:
            self.db.close()
            print("Acceso denegado.")

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
