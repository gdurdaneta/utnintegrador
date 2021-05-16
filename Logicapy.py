#from Main_Windows_base import Ui_MainWindow
from modelobd import OperacionesBaseDatos
#from funcionescnclase import ingresarusuario.borrar


class Logica():

    def __init__(self):
        self.nombre = ''
        self.apellido = '' 
        self.dni = 0
        self.sexo = ''
        self.telefono = 0
        self.usuario = ''
        self.password = ''
        self.variable = ""
        self.datomodificar = ""
        
    def realizaroperacion():
        while True:
            print("""Bienvenido, elija la opcion deseada:\n
            [1] - Crear Usuario:
            [2] - Modifica Usuario:
            [3] - Borra Usuario:
            [4] - Consulta Usuario:
            [5] - Salir.
            """)

            opccion = int(input("ingrese su opccion"))
            if opccion == 1:
                Logica.creausuario
            elif opccion == 2:
                Logica.modifica
            elif opccion == 3:
                Logica.borra
            elif opccion == 4:
                Logica.consulta
            elif opccion == 5:
                break
            else:
                print("opcion incorrecta")

    def creausuario(self):
        print("\nMenu para la creacion de usuarios:\n")

        self.usuario = input("Ingrese el usuario: ")
        self.password = input("Ingrese el password: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.sexo = input("Ingrese el sexo: ")
        self.telefono = int(input("Ingrese el numero de celular: "))
        self.dni = int(input("Ingrese el DNI: "))

        OperacionesBaseDatos.creausuario(Logica.guardardatos)

    def modifica(self):
        print("Menu de modificacion de usuarios: \n")
        print("""Que dato desea modificar: 
                [1] - Nombre
                [2] - Apellido   
                [3] - Sexo
                [4] - Telefono
                [5] - DNI
                [6] - Realizar otra operacion
                """)
        datomodificar = int(input("Ingrese el dato a modificar: "))
        variablemodificar = ""
        nuevodato = ""

        if datomodificar == 1:
            variablemodificar = "nombre"
            nuevodato = input("Ingrese el nombre: ")
        elif datomodificar == 2:       
            variablemodificar = "apellido"
            nuevodato = input("Ingrese el apellido: ")
        elif datomodificar == 3:
            variablemodificar = "sexo"#para ser lgbtqwerty friendly
            nuevodato = input("Ingrese el sexo: ")
        elif datomodificar == 4:
            variablemodificar = "telefono"
            nuevodato = int(input("Ingrese el numero de telefono: "))
        elif datomodificar == 5 :
            variablemodificar = "DNI"
            nuevodato = int(input("Ingrese el numero de DNI: "))
        elif datomodificar == 6:
            Logica.realizaroperacion
            
    def borra(self):
        print("\nMenu para borrar informacion:\n")
        print("\nIngrese el usuario a borrar")
        self.usuario = input("Ingrese su usuario ")
        self.password = input("Ingrese su password ")
        OperacionesBaseDatos.borrar(self, self.usuario, self.password)

    def consulta(self):
        self.usuario = input("Ingrese el Usuario a consultar ")
        OperacionesBaseDatos.consultageneral(self.usuario)

    def guardardatos(self):
        self.lista.append = [self.usuario, self.apellido, self.nombre, self.apellido, self.dni, self.sexo, self.telefono]

    def login(self):
        badpassword = 0
        print("Binvenido")
        print("Tiene usuario o desea crear uno")
        opcion = int(input("Oprima 1 para crear un usuario o 2 para ingresar con su usuairo"))
        if opcion == 1:
            Logica.realizaroperacion()
        elif opcion == 2:    
            try:
                self.usuario = input("Ingrese su usario ")
                if self.usuario == OperacionesBaseDatos.consutaindividual:
                    while badpassword <= 3:
                        self.password = input("Ingrese su password")
                        if self.password == OperacionesBaseDatos.consulta[2]:
                            Logica.realizaroperacion
                        else:
                            print("Password equicada")
                            badpassword += 1
            except:
                print("algo salio mal ...")
        else:
            print("opcion incorrecta ")

