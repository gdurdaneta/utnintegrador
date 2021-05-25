from visualbase import App
from modelobd import OperacionDB
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import re


class loginApp:
    """
    Se crea clase para la visual del login y sus componentes
    """
    def __init__(self, root):
        """
        Se establecen valores de variables y configuracion de la visual del login.
        """
        root.title("Integrador UTN")
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)
        usuarioLabel=tk.Label(root)

        usuarioLabel["fg"] = "#333333"
        usuarioLabel["justify"] = "center"
        usuarioLabel["text"] = "Usuario"
        usuarioLabel.place(x=50,y=160,width=70,height=25)

        passwordLabel=tk.Label(root)

        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Password"
        passwordLabel.place(x=50,y=200,width=70,height=25)

        ingresarBotton=tk.Button(root)
        ingresarBotton["bg"] = "#fafafa"
        ingresarBotton["fg"] = "#3d3d3d"
        ingresarBotton["justify"] = "center"
        ingresarBotton["text"] = "Ingresar"
        ingresarBotton.place(x=70,y=280,width=70,height=25)
        ingresarBotton["command"] = self.IngressBotton

        crearBotton=tk.Button(root)
        crearBotton["bg"] = "#fafafa"
        crearBotton["fg"] = "#3d3d3d"
        crearBotton["justify"] = "center"
        crearBotton["text"] = "Crear"
        crearBotton.place(x=170,y=280,width=70,height=25)
        crearBotton["command"] = self.CreateBotton

        self.usuarioEntry=tk.Entry(root)
        self.usuarioEntry["borderwidth"] = "1px"

        self.usuarioEntry["fg"] = "#333333"
        self.usuarioEntry["justify"] = "center"
        self.usuarioEntry["text"] = "Usuario Entry"
        self.usuarioEntry.place(x=140,y=160,width=100,height=25)

        self.passwordEntry=tk.Entry(root)
        self.passwordEntry["borderwidth"] = "1px"

        self.passwordEntry["fg"] = "#333333"
        self.passwordEntry["justify"] = "center"
        self.passwordEntry["text"] = "Password Entry"
        self.passwordEntry.place(x=140,y=200,width=100,height=25)

        urdantemsg=tk.Label(root)
        urdantemsg["justify"] = "right"
        urdantemsg["text"] = "Gerardo Urdaneta"
        urdantemsg.place(x=140,y=430,width=150,height=50)

        franciscomsg=tk.Label(root)
        franciscomsg["justify"] = "right"
        franciscomsg["text"] = "Francisco Bryndum"
        franciscomsg.place(x=140,y=400,width=150,height=30)

    def IngressBotton(self):
        """
        Metodo destinado para llamar a la funcion de modelobd.py, clase OperacionesDB / funcion ingresousuarios
        Si esta OK, llama otra ventana y se destruye el login.
        Caso contrario ventana de error.
        """
        try:
            ingreso = OperacionDB().ingresousuarios((self.usuarioEntry.get()), (self.passwordEntry.get()))
            if ingreso == True:
                rootlogin.destroy()
                root = tk.Tk()    
                baseapp = App(root)
                root.mainloop()
            else:
                messagebox.showinfo(message="Combinación de usuario y password incorrecta!", title="Acceso denegado.")
        except:
            pass

    def CreateBotton(self):
        """
        Este metodo lo que hace es tomar la accion de destuir la ventana de login e iniciar la ventana de crear.
        """
        rootlogin.destroy()
        root = tk.Tk()
        baseapp = baseApp(root)
        root.mainloop()
            
    def iniciar():
        """
        Este metodo lo que hace es iniciar la ventana loginApp.
        """
        rootlogin = tk.Tk()
        app = loginApp(rootlogin)
        rootlogin.mainloop()

class baseApp:
    """
    Clase para la ventana de creacion de usuarios. Se establecen variables y la visual de la ventana.
    """
    def __init__(self, root):
        """
        Configuracion de la visual de la ventana para creacion de usuarios.
        """
        root.title("Integrador UTN")
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)

        dniLabel=tk.Label(root)
        dniLabel["fg"] = "#333333"
        dniLabel["justify"] = "center"
        dniLabel["text"] = "DNI"
        dniLabel.place(x=50,y=200,width=70,height=25)

        self.apellidoEntry=tk.Entry(root)
        self.apellidoEntry["borderwidth"] = "1px"
        self.apellidoEntry["fg"] = "#333333"
        self.apellidoEntry["justify"] = "left"
        self.apellidoEntry["text"] = "Apellido_entry"
        self.apellidoEntry["relief"] = "sunken"
        self.apellidoEntry.place(x=140,y=160,width=141,height=30)

        self.dniEntry=tk.Entry(root)
        self.dniEntry["borderwidth"] = "1px"
        self.dniEntry["fg"] = "#333333"
        self.dniEntry["justify"] = "left"
        self.dniEntry["text"] = "Dni_entry"
        self.dniEntry["relief"] = "sunken"
        self.dniEntry.place(x=140,y=200,width=142,height=30)

        crearBotton=tk.Button(root)
        crearBotton["bg"] = "#fafafa"
        crearBotton["fg"] = "#3d3d3d"
        crearBotton["justify"] = "center"
        crearBotton["text"] = "Crear"
        crearBotton.place(x=10,y=300,width=70,height=25)
        crearBotton["command"] = self.crearBotton_command

        nombreLabel=tk.Label(root)
        nombreLabel["fg"] = "#333333"
        nombreLabel["justify"] = "center"
        nombreLabel["text"] = "Nombre"
        nombreLabel.place(x=50,y=120,width=70,height=25)

        passwordLabel=tk.Label(root)
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Password"
        passwordLabel.place(x=50,y=80,width=70,height=25)

        self.nombreEntry=tk.Entry(root)
        self.nombreEntry["borderwidth"] = "1px"
        self.nombreEntry["fg"] = "#333333"
        self.nombreEntry["justify"] = "left"
        self.nombreEntry["text"] = "Nombre_entry"
        self.nombreEntry["relief"] = "sunken"
        self.nombreEntry.place(x=140,y=120,width=140,height=30)

        self.passwordEntry=tk.Entry(root)
        self.passwordEntry["borderwidth"] = "1px"
        self.passwordEntry["fg"] = "#333333"
        self.passwordEntry["justify"] = "left"
        self.passwordEntry["text"] = "Password_entry"
        self.passwordEntry["relief"] = "sunken"
        self.passwordEntry.place(x=140,y=80,width=141,height=30)

        usuarioLabel=tk.Label(root)
        usuarioLabel["fg"] = "#333333"
        usuarioLabel["justify"] = "center"
        usuarioLabel["text"] = "Usuario"
        usuarioLabel.place(x=50,y=40,width=70,height=25)

        self.usuarioEntry=tk.Entry(root)
        self.usuarioEntry["borderwidth"] = "1px"
        self.usuarioEntry["fg"] = "#333333"
        self.usuarioEntry["justify"] = "left"
        self.usuarioEntry["text"] = "Usuario_entry"
        self.usuarioEntry["relief"] = "sunken"
        self.usuarioEntry.place(x=140,y=40,width=141,height=30)

        telefonoLabel=tk.Label(root)
        telefonoLabel["anchor"] = "n"
        telefonoLabel["fg"] = "#333333"
        telefonoLabel["justify"] = "center"
        telefonoLabel["text"] = "Telefono"
        telefonoLabel.place(x=50,y=240,width=70,height=25)

        self.telefonoEntry=tk.Entry(root)
        self.telefonoEntry["borderwidth"] = "1px"
        self.telefonoEntry["fg"] = "#333333"
        self.telefonoEntry["justify"] = "left"
        self.telefonoEntry["text"] = "Telefono_entry"
        self.telefonoEntry["relief"] = "sunken"
        self.telefonoEntry.place(x=140,y=240,width=140,height=30)

        apellidoLabel=tk.Label(root)
        apellidoLabel["fg"] = "#333333"
        apellidoLabel["justify"] = "center"
        apellidoLabel["text"] = "Apellido"
        apellidoLabel.place(x=50,y=160,width=70,height=25)
        
    def crearBotton_command(self):
        """
        Este metodo genera una lista con los entry de la ventana para crear usuarios.
        Luego las utiliza para llamar la funcion de crear usuario en la clase OperacionDB.
        Confirma la creacion o el error.
        """
        
        patron = re.compile(r'''(
                            ^(?=.*[A-Z])
                            (?=.*[a-z])
                            (?=.*[0-9])
                            (?=.*[!@#$%&])
                            .{8,}
                            $
                            )''', re.VERBOSE)

        if patron.search(self.passwordEntry.get()) == True:
                
            try:
                lista = [self.usuarioEntry.get(), self.passwordEntry.get(), self.nombreEntry.get(),
                        self.apellidoEntry.get(), self.dniEntry.get(), self.telefonoEntry.get()
                ]
                OperacionDB().creausuario(lista)
                messagebox.showinfo(message="Usuario Creado Correctamente", title="Alerta!")
            except:
                messagebox.showinfo(message="Error, el usuario no se creo.", title="Alerta!")
        else:
            messagebox.showerror(message="La contraseña no cumple con los requisitos", title="Alerta")
            messagebox.showerror(message="La contraseña debe tener 8 caracteres, Mayusculas y minusculas", title="Alerta")
        
if __name__ == "__main__":
    rootlogin = tk.Tk()
    app = loginApp(rootlogin)
    rootlogin.mainloop()
