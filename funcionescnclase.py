
from datetime import date

class operacionesbasedatos:

    def __init__(self):

        pass

    def conexion (self, db, dbcursor):

        import sqlite3

        #Crea conexion con base de datos, sino existe crea la base de datos "turnossede"

        db = sqlite3.connect("usuarios.db")
        dbcursor = db.cursor() # Es el cursor en la base de datos

        #Crea la tabla de turnos y si ya existe, se conecta.

    def crearbaseytabla(self):

        conexion(db, dbcursor)

        #Intenta crear base de datos.

        try:
            dbcursor.execute('''CREATE TABLE usuarios (Usuario text NOT NULL, Nombre text NOT NULL, Apellido text NOT NULL, Sexo text NOT NULL, telefono integer NOT NULL, Password text NOT NULL, DNI integer NOT NULL)''')
            db.commit()
            print("Creacion de base de datos y tabla OK.")

        #Si ya existe confirma su conexion.

        except:
            print("Conexion exitosa.")

    def ingresarusuario(self, usuario, nombre, apellido, sexo, telefono, password, dni):

        conexion(db, dbcursor)

        '''
        Esto se modifica con ingresos del main windows
        '''

        usuario = input("Usuario: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        sexo = input("Ingrese su sexo: ")
        telefono = int(input("Ingrese su numero de celular: "))
        password = input("Ingrese su Password: ")
        dni = int(input("Ingrese el DNI: "))

        dbcursor.execute(
            "INSERT INTO usuarios (usuario, nombre, apellido, sexo, telefono, password, dni) VALUES (?, ?, ?, ?, ?, ? ,?)",
            (usuario, nombre, apellido, sexo, telefono, password, dni))
        db.commit()

        db.close()
        
        print("Carga OK.")

    def borrar(self, usuario, password):

        conexion(db, dbcursor)

        usuario = input("Ingrese su nombre: ")
        password = input("Ingrese su apellido: ")

        try:

            dbcursor.execute("DELETE FROM usuarios WHERE usuario =? and password =?",(usuario, password))

            db.commit()

            db.close()

            print("Borrado exitoso.")
        
        except:
            ("Convinacion de usuario y contraseña invalido.")

    def borrartodo(self):

        conexion(db, dbcursor)

        dbcursor.execute("DROP TABLE usuarios")

        db.close()

        print("Borrado completo.")

    def buscardatos(self, usuario, password):

        conexion(db, dbcursor)
        
        usuario = input("Ingrese el usuario: ")
        password= input("Ingrese el contraseña: ")

        try:
            dbcursor.execute("SELECT * FROM usuarios WHERE usuario=? AND password =?", (usuario, password))
            busqueda = dbcursor.fetchone()
            if busqueda is not None:
                print(f"Datops del usuario: {busqueda}")
            else:
                print("No hay ningun turno con ese nombre.")
        except:
            print("Ingrese un usuario y password valido.")

            db.close()

    



    
    
    
    
    