from funcionescnclase import operacionesbasedatos



class Inicio ():

    def __init__(self):
        self.usuario = "demo"
        self.password = "demo"
        self.opcion = 0
        self.contador = 3
        self.opcionborrado = 0
        
    def login(self):

        print("""Bienvenido, elija la opcion deseada:\n
            [1] - Ingreso de usuario:
            [2] - Crear usuario:
            [3] - Modificar:
            [4] - Borrar:
            [5] - Salir.        
                    """)
        self.opcion = int(input("ingrese una opcion"))
        self.opciones = {
            1,2,3,4,5
        }

        if self.opcion in self.opciones:
            
            if self.opcion == 1:

                ingreso(self)
                try:
                    operacionesbasedatos().buscardatos(self.usuario, self.password)
                except:
                    pass
                finally:
                    pass

            elif self.opcion == 2:

                creacion(self)
                operacionesbasedatos().ingresarusuario(self.usuario, self.nombre, self.apellido, self.sexo, self.telefono, self.password, self.dni)

            elif self.opcion == 3:

                modificacion (self)
                operacionesbasedatos().modificarusuario(self.usuario, self.password)

            elif self.opcion == 4:

                borrado(self)
                operacionesbasedatos().borrar(self.usuario, self.password)

        else:
            print("Ingrese una opcion valida.")
    
def ingreso (self):

    while self.contador != 0:

        try: 

            print("\nMenu de acceso a usuarios:\n")
            self.usuario = input("Ingrese su usuario: ")
            self.password = input("Ingrese su contraseña: ")

            #Conexion con funciones con clase, buscar datos en base. Cambio self contador = 0 para cortar area de acceso usuarios.

            #self.basedatos.Conexion()

            #basedatos.crearbaseytabla()

            #base.buscardatos()

            self.contador = 0

            print("Acceso correcto!.")

        except:

            #Si la convinacion es erronea, resto 1 contador, informo error y continuo solicitando ingreso.

            self.contador -= 1

            print(F"""Convinacion de usuario y contraseña invalido. 
                                Le quedan {self.contador} intentos.
                    """)
    
    if self.contador == 0:

        print("Acceso denegado.")

        

def creacion (self):

    print("\nMenu de creacion de usuarios:\n")

    self.usuario = input("Ingrese el usuario: ")
    self.nombre = input("Ingrese el nombre: ")
    self.apellido = input("Ingrese el apellido: ")
    self.sexo = input("Ingrese el sexo: ")
    self.telefono = int(input("Ingrese el numero de celular: "))
    self.password = input("Ingrese el password: ")
    self.dni = int(input("Ingrese el DNI: "))

    #Conexion con funciones con clase, crear usuario.

    #basedatos.ingresarusuario()

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
        pass
        #inicio(self)

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

        opcionborrado = int(input("Ingrese la opcion deseada: "))

        if opcionborrado == 1:

            try:

                #Conexion con borrado de base de datos.
                print("Usuario borrado.")

                estadoborrado == True
            
            except:
                print("Convinacion de usuario y contraseña invalido.")

                contadorborrado -= 1

        elif opcionborrado == 2:
            
            #basedatos.borrartodo()

            estadoborrado == True

        else:
            print("Ingrese una opcion valida.\n")

            #Conexon con borrado total de base de datos.



Inicio().login()



