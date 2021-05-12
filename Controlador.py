from funcionescnclase import operacionesbasedatos



class Inicio ():

    def __init__(self):
        self.usuario = "demo"
        self.password = "demo"
        print("""Bienvenido, elija la opcion deseada:\n
            [1] - Ingreso de usuario:
            [2] - Crear usuario:
            [3] - Modificar:
            [4] - Borrar:
            [5] - Salir.        
                    """)

        self.contador = 3

        self.opciones = {
            1,2,3,4,5
        }
        

    def inicio():
        pass
    
    def login(self, opcion):

        if opcion in self.opciones:
            
            if opcion == 1:
                self.usuario = input("ingrese su usuario")
                self.password = input("ingrese su password")
                operacionesbasedatos().buscardatos(usuario, password)
                

            elif opcion == 2:

                creacion(self)
                operacionesbasedatos().ingresarusuario(usuario, nombre, apellido, sexo, telefono, password, dni)

            elif opcion == 3:

                modificacion (self)
                operacionesbasedatos().modificarusuario(usuario, password)

            elif opcion == 4:

                borrado(self)
                operacionesbasedatos().borrar(usuario, password)

        else:
            print("Ingrese una opcion valida.")
    
def ingreso (self):

    while self.contador != 0:

        try: 

            print("Menu de acceso a usuarios:\n")
            self.usuario = input("Ingrese su usuario: ")
            self.password = input("Ingrese su contraseña: ")

            #Conexion con funciones con clase, buscar datos en base. Cambio self contador = 0 para cortar area de acceso usuarios.

            basedatos.Conexion()

            basedatos.crearbaseytabla()

            base.buscardatos()

            self.contador = 0

            print("Acceso correcto!.")

        except:

            #Si la convinacion es erronea, resto 1 contador, informo error y continuo solicitando ingreso.

            self.contador -= 1

            print("""Convinacion de usuario y contraseña invalido. 
            Le quedan {self.contador} intentos.
            """)

def creacion (self):

    print("Menu de creacion de usuarios:\n")

    self.usuario = input("Ingrese el usuario: ")
    self.nombre = input("Ingrese el nombre: ")
    self.apellido = input("Ingrese el apellido: ")
    self.sexo = input("Ingrese el sexo: ")
    self.telefono = int(input("Ingrese el numero de celular: "))
    self.password = input("Ingrese el password: ")
    self.dni = int(input("Ingrese el DNI: "))

    #Conexion con funciones con clase, crear usuario.

    basedatos.ingresarusuario()

def modificacion (self):

    print("Menu de modificacion de usuarios: \n")

    self.usuario = input("Ingrese el usuario: ")
    self.password = input ("Ingrese la password: ")

    #Si usuario y contraseña OK:

    print("""Que dato desea modificar: 
    [1] - Nombre
    [2] - Apellido   
    [3] - Sexo
    [4] - Telefono
    [5] - DNI
    [6] - Salir
    """)

    datomodificar = input("Ingrese el dato a modificar: ")

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

        inicio(self)

    else:
        
        print("Ingrese una opcion valida.")

        modificacion(self)


def borrado ():

    estadoborrado = False

    contadorborrado = 3

    print("""Menu de borrado de usuarios:
    
[1] - Borrado de usario.
[2] - Borrado de base de datos.
    """)

    while estadoborrado == False and contadorborrado != 0:

        self.opcionborrado = input("Ingrese la opcion deseada: ")

        if self.opcionborrado == 1:

            try:

                #Conexion con borrado de base de datos.
                print("Usuario borrado.")

                estadoborrado == True
            
            except:
                print("Convinacion de usuario y contraseña invalido.")

                contadorborrado -= 1

        elif self.opcionborrado == 2:
            
            basedatos.borrartodo()

            estadoborrado == True

        else:
            print("Ingrese una opcion valida.\n")

            #Conexon con borrado total de base de datos.

iniciar = Inicio()
iniciar.login(opcion = int(input("Ingrese la opcion deseada: ")))



