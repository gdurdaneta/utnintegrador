from funcionescnclase import operacionesbasedatos

class Inicio ():

    def __init__(self):

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
        
    def login(self, opcion):

        if opcion in self.opciones:
            
            if opcion == 1:
                
                ingreso(self)

            elif opcion == 2:

                creacion(self)

            elif opcion == 3:

                modificacion (self)

            elif opcion == 4:

                borrado(self)

        else:
            print("Ingrese una opcion valida.")
    
def ingreso (self):

    while self.contador != 0:

        try: 

            print("Menu de acceso a usuarios:\n")
            self.usuario = input("Ingrese su usuario: ")
            self.password = input("Ingrese su contraseña: ")

            #Conexion con funciones con clase, buscar datos en base. Cambio self contador = 0 para cortar area de acceso usuarios.

            self.contador = 0

            print("Acceso correcto!.")

        except:

            #Si la convinacion es erronea, resto 1 contador, informo error y continuo solicitando ingreso.

            self.contador -= 1

            print("""Convinacion de usuario y contraseña invalido. 
            Le quedan {Self.contador} intentos.
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
    """)

    datomodificar = input("Ingrese el dato a modificar: ")

    if datomodificar == 1:
        print("Modifica nombre ")
    elif datomodificar == 2:
        print("modifica Apellido")
    elif datomodificar == 3:
        print("Modifica sexo") #para ser lgbtqwerty friendly
    elif datomodificar == 4:
        print("Modifica telefono")
    elif datomodificar == 5 :
        print("Modifica DNI")
    else:
        print("ha elegido una opcion invalida")


    

def borrado ():

    print("""Menu de borrado de usuarios:
    
[1] - Borrado de usario.
[2] - Borrado de base de datos.
    """)

    self.opcionborrado = input("Ingrese la opcion deseada: ")

    if self.opcionborrado == 1:

        try:
            #Conexion con borrado de base de datos.
            print("Usuario borrado.")
        
        except:
            print("Convinacion de usuario y contraseña invalido.")

    elif self.opcionborrado == 2:

        print("Base de datos borrada.")

        #Conexon con borrado total de base de datos.



iniciar = Inicio()
iniciar.login(opcion = int(input("Ingrese la opcion deseada: ")))



