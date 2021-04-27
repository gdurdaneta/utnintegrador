import sqlite3
from datetime import date

class operacionesbasedatos:

    def __init__(self):

        self.db = sqlite3.connect("database.db")
        self.dbcursor = self.db.cursor()
        #self.conexion = self.db.conexion()
     


    def conexion (self, db, dbcursor):
        #Crea conexion con base de datos, sino existe crea la base de datos "turnossede"
        self.db = sqlite3.connect("usuarios.db")
        self.dbcursor = db.cursor() # Es el cursor en la base de datos
        #Crea la tabla de turnos y si ya existe, se conecta.

    def crearbaseytabla(self):
        # self.conexion(db, dbcursor)
        #Intenta crear base de datos.
        try:
            self.dbcursor.execute('''CREATE TABLE usuarios (Usuario text NOT NULL, Nombre text NOT NULL, Apellido text NOT NULL, Sexo text NOT NULL, telefono integer NOT NULL, Password text NOT NULL, DNI integer NOT NULL)''')
            self.db.commit()
            print("Creacion de base de datos y tabla OK.")

        #Si ya existe confirma su conexion.

        except:
            print("Conexion exitosa.")

    def ingresarusuario(self, usuario, nombre, apellido, sexo, telefono, password, dni):

        self.conexion(db, dbcursor)

        '''
        Esto se modifica con ingresos del main windows
        '''

        self.usuario = input("Usuario: ")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.sexo = input("Ingrese su sexo: ")
        self.telefono = int(input("Ingrese su numero de celular: "))
        self.password = input("Ingrese su Password: ")
        self.dni = int(input("Ingrese el DNI: "))

        dbcursor.execute(
            "INSERT INTO usuarios (usuario, nombre, apellido, sexo, telefono, password, dni) VALUES (?, ?, ?, ?, ?, ? ,?)",
            (usuario, nombre, apellido, sexo, telefono, password, dni))
        db.commit()

        db.close()
        
        print("Carga OK.")

    def borrar(self, usuario, password):

        self.conexion(db, dbcursor)

        self.usuario = input("Ingrese su nombre: ")
        self.password = input("Ingrese su apellido: ")

        try:

            self.dbcursor.execute("DELETE FROM usuarios WHERE usuario =? and password =?",(usuario, password))

            self.db.commit()

            self.db.close()

            print("Borrado exitoso.")
        
        except:
            ("Convinacion de usuario y contraseña invalido.")

    def borrartodo(self):

        self.conexion(db, dbcursor)

        self.dbcursor.execute("DROP TABLE usuarios")

        self.db.close()

        print("Borrado completo.")

    def buscardatos(self, usuario, password):

        self.conexion(db, dbcursor)
        
        self.usuario = input("Ingrese el usuario: ")
        self.password= input("Ingrese el contraseña: ")

        try:
            self.dbcursor.execute("SELECT * FROM usuarios WHERE usuario=? AND password =?", (usuario, password))
            busqueda = dbcursor.fetchone()
            if busqueda is not None:
                print(f"Datops del usuario: {busqueda}")
            else:
                print("No hay ningun turno con ese nombre.")
        except:
            print("Ingrese un usuario y password valido.")

            self.db.close()
