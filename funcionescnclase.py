import sqlite3

class OperacionesBaseDatos:

    def __init__(self):

        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        self.contador = 3

    #def conexion (self, db):
        #Crea conexion con base de datos, sino existe crea la base de datos "turnossede"
        #self.db = sqlite3.connect("usuarios.db")
        #self.dbcursor = db.cursor() # Es el cursor en la base de datos
        #Crea la tabla de turnos y si ya existe, se conecta.


    def crearbaseytabla2(self):
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

    def crearbaseytabla(self):
        # self.conexion(db, dbcursor)
        #Intenta crear base de datos.
        try:
            self.dbcursor.execute('''CREATE TABLE usuarios (Usuario text NOT NULL, Password text NOT NULL, Nombre text NOT NULL, Apellido text NOT NULL, Sexo text NOT NULL, telefono integer NOT NULL, DNI integer NOT NULL)''')
            self.db.commit()
            print("Creacion de base de datos y tabla OK.")

        #Si ya existe confirma su conexion.

        except:
            print("\nConexion exitosa.\n")

    def creausuarios(self, usuario, nombre, apellido, sexo, telefono, password, dni):

        print("\nMenu para la creacion de usuarios:\n")

        self.usuario = input("Ingrese el usuario: ")
        self.password = input("Ingrese el password: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.sexo = input("Ingrese el sexo: ")
        self.telefono = int(input("Ingrese el numero de celular: "))
        self.dni = int(input("Ingrese el DNI: "))

        self.dbcursor.execute(
            "INSERT INTO integrador (Usuario, Password, Nombre, Apellido, Sexo, Telefono, Dni) VALUES (?, ?, ?, ?, ?, ? ,?)",
            (self.usuario, self.password, self.nombre, self.apellido, self.sexo, self.telefono, self.dni))
        self.db.commit()

        self.db.close()
        
        print("\n Se ha creado el usuario.\n")

    def borrar(self, usuario, password):

        print("\nMenu para borrar informacion:\n")

        self.usuario = input("Ingrese el usuario: ")
        self.password = input("Ingrese el password: ")

        try:

            self.dbcursor.execute("DELETE FROM integrador WHERE usuario =? and password =?",(self.usuario, self.password))

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

    def modificarusuario (self,usuario, password, datomodificar, nuevodato, variablemodificar):

            print("Menu de modificacion de usuarios: \n")

            print("""Que dato desea modificar:

[1] - Nombre
[2] - Apellido   
[3] - Sexo
[4] - Telefono
[5] - DNI
[6] - Salir
            """)

            self.datomodificar = int(input("\nIngrese el dato a modificar: "))

            self.variablemodificar = ""
            self.nuevodato = ""

            if self.datomodificar == 1:
                
                self.variablemodificar = "Nombre"

                self.nuevodato = input("Ingrese el nombre: ")

            elif self.datomodificar == 2:
                
                self.variablemodificar = "Apellido"

                self.nuevodato = input("Ingrese el apellido: ")

            elif self.datomodificar == 3:

                self.variablemodificar = "Sexo"#para ser lgbtqwerty friendly

                self.nuevodato = input("Ingrese el sexo: ")

            elif self.datomodificar == 4:

                self.variablemodificar = "Telefono"

                self.nuevodato = int(input("Ingrese el numero de telefono: "))

            elif self.datomodificar == 5 :

                self.variablemodificar = "Dni"

                self.nuevodato = int(input("Ingrese el numero de DNI: "))

            elif self.datomodificar == 6:
                pass
                Inicio(self)

            else:
        
                print("Ingrese una opcion valida.")

            self.usuario = input("Ingrese el usuario: ")
            self.password = input ("Ingrese el password: ")

            try:
                self.dbcursor.execute("SELECT nombre FROM integrador WHERE Usuario=? AND Password =?", (self.usuario, self.password))
                self.db.commit()
                busqueda = self.dbcursor.fetchone()
                if busqueda is not None:

                    self.dbcursor.execute("UPDATE integrador SET {self.variablemodificar} =? WHERE usuario =? AND password =?", (self.nuevodato,self.usuario,self.password))

                    print("Modificacion realizada con exito.")

                else:

                    print("Convinación de usuario y contraseña incorrecta.")

            except sqlite3.OperationalError:
                print(sqlite3.OperationalError)
                print("Ingrese una convinación valida.")


OperacionesBaseDatos().crearbaseytabla2()