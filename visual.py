
from typing import get_args
from logica import logica
import tkinter as tk
import tkinter.font as tkFont
#from PIL import ImageTk, Image
import os

class loginApp:
    def __init__(self, root):
        #setting title
        root.title("Integrador UTN")
        #setting window size
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)
        usuarioLabel=tk.Label(root)
        #usuarioLabel["font"] = ft
        usuarioLabel["fg"] = "#333333"
        usuarioLabel["justify"] = "center"
        usuarioLabel["text"] = "Usuario"
        usuarioLabel.place(x=50,y=160,width=70,height=25)

        passwordLabel=tk.Label(root)
        # passwordLabel["font"] = ft
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Password"
        passwordLabel.place(x=50,y=200,width=70,height=25)

        ingresarBotton=tk.Button(root)
        ingresarBotton["bg"] = "#fafafa"
        
        #ingresarBotton["font"] = ft
        ingresarBotton["fg"] = "#3d3d3d"
        ingresarBotton["justify"] = "center"
        ingresarBotton["text"] = "Ingresar"
        ingresarBotton.place(x=70,y=280,width=70,height=25)
        ingresarBotton["command"] = self.IngressBotton

        crearBotton=tk.Button(root)
        crearBotton["bg"] = "#fafafa"
        # crearBotton["font"] = ft
        crearBotton["fg"] = "#3d3d3d"
        crearBotton["justify"] = "center"
        crearBotton["text"] = "Crear"
        crearBotton.place(x=170,y=280,width=70,height=25)
        crearBotton["command"] = self.CreateBotton

        self.usuarioEntry=tk.Entry(root)
        self.usuarioEntry["borderwidth"] = "1px"
        # usuarioEntry["font"] = ft
        self.usuarioEntry["fg"] = "#333333"
        self.usuarioEntry["justify"] = "center"
        self.usuarioEntry["text"] = "Usuario Entry"
        self.usuarioEntry.place(x=140,y=160,width=100,height=25)

        self.passwordEntry=tk.Entry(root)
        self.passwordEntry["borderwidth"] = "1px"
        self.passwordEntry["font"] = ft
        self.passwordEntry["fg"] = "#333333"
        self.passwordEntry["justify"] = "center"
        self.passwordEntry["text"] = "Password Entry"
        self.passwordEntry.place(x=140,y=200,width=100,height=25)

        # logo = Imagetk.PhotoImage(Image.open("logo.gif"))
        # logo.place(x=120,y=150,width=100,height=25)

        urdantemsg=tk.Label(root)
        # passwordLabel["font"] = ft
        #urdantemsg["fg"] = "#333333"
        urdantemsg["justify"] = "right"
        urdantemsg["text"] = "Gerardo Urdaneta"
        urdantemsg.place(x=140,y=430,width=150,height=50)

        franciscomsg=tk.Label(root)
        # passwordLabel["font"] = ft
        #franciscomsg["fg"] = "#333333"
        franciscomsg["justify"] = "right"
        franciscomsg["text"] = "Francisco Bryndum"
        franciscomsg.place(x=140,y=400,width=150,height=30)


    def IngressBotton(self):
        try:
            logica.botoningreso(self.usuarioEntry, self.passwordEntry)
        except:
            print("error")
        finally:
            rootlogin.destroy()
            root = tk.Tk()    
            baseapp = baseApp(root)
            root.mainloop()
            print("command")


    def CreateBotton(self):
        try:
            logica.botoncrear(self.usuarioEntry, self.passwordEntry, self.apellidoEntry,self.dniEntry, self.nombreEntry, self.telefonoEntry)
        except:
            print("error")
        finally:
            rootlogin.destroy()
            root = tk.Tk()
            baseapp = baseApp(root)
            root.mainloop()
            print("command")

    def iniciar():
        rootlogin = tk.Tk()
        app = loginApp(rootlogin)
        rootlogin.mainloop()

class baseApp:
    def __init__(self, root):
        #setting title
        root.title("Integrador UTN")
        #setting window size
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)

        dniLabel=tk.Label(root)
        # dniLabel["font"] = ft
        dniLabel["fg"] = "#333333"
        dniLabel["justify"] = "center"
        dniLabel["text"] = "DNI"
        dniLabel.place(x=50,y=200,width=70,height=25)

        contultarBotton=tk.Button(root)
        contultarBotton["bg"] = "#fafafa"
        # contultarBotton["font"] = ft
        contultarBotton["fg"] = "#3d3d3d"
        contultarBotton["justify"] = "center"
        contultarBotton["text"] = "Consultar"
        contultarBotton.place(x=250,y=300,width=70,height=25)
        contultarBotton["command"] = self.consultarBotton_command

        eliminarBotton=tk.Button(root)
        eliminarBotton["bg"] = "#fafafa"
        # eliminarBotton["font"] = ft
        eliminarBotton["fg"] = "#3d3d3d"
        eliminarBotton["justify"] = "center"
        eliminarBotton["text"] = "Eliminar"
        eliminarBotton.place(x=170,y=300,width=70,height=25)
        eliminarBotton["command"] = self.eliminarBotton_command

        self.apellidoEntry=tk.Entry(root)
        self.apellidoEntry["borderwidth"] = "1px"
        # apellidoEntry["font"] = ft
        self.apellidoEntry["fg"] = "#333333"
        self.apellidoEntry["justify"] = "left"
        self.apellidoEntry["text"] = "Apellido_entry"
        self.apellidoEntry["relief"] = "sunken"
        self.apellidoEntry.place(x=140,y=160,width=141,height=30)

        self.dniEntry=tk.Entry(root)
        self.dniEntry["borderwidth"] = "1px"
        # dniEntry["font"] = ft
        self.dniEntry["fg"] = "#333333"
        self.dniEntry["justify"] = "left"
        self.dniEntry["text"] = "Dni_entry"
        self.dniEntry["relief"] = "sunken"
        self.dniEntry.place(x=140,y=200,width=142,height=30)

        crearBotton=tk.Button(root)
        crearBotton["bg"] = "#fafafa"
        # crearBotton["font"] = ft
        crearBotton["fg"] = "#3d3d3d"
        crearBotton["justify"] = "center"
        crearBotton["text"] = "Crear"
        crearBotton.place(x=10,y=300,width=70,height=25)
        crearBotton["command"] = self.crearBotton_command

        modificarBotton=tk.Button(root)
        modificarBotton["bg"] = "#fafafa"
        # modificarBotton["font"] = ft
        modificarBotton["fg"] = "#3d3d3d"
        modificarBotton["justify"] = "center"
        modificarBotton["text"] = "Modificar"
        modificarBotton.place(x=90,y=300,width=70,height=25)
        modificarBotton["command"] = self.modificarBotton_command

        nombreLabel=tk.Label(root)
        # nombreLabel["font"] = ft
        nombreLabel["fg"] = "#333333"
        nombreLabel["justify"] = "center"
        nombreLabel["text"] = "Nombre"
        nombreLabel.place(x=50,y=120,width=70,height=25)

        passwordLabel=tk.Label(root)
        # passwordLabel["font"] = ft
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Password"
        passwordLabel.place(x=50,y=80,width=70,height=25)

        self.nombreEntry=tk.Entry(root)
        self.nombreEntry["borderwidth"] = "1px"
        # nombreEntry["font"] = ft
        self.nombreEntry["fg"] = "#333333"
        self.nombreEntry["justify"] = "left"
        self.nombreEntry["text"] = "Nombre_entry"
        self.nombreEntry["relief"] = "sunken"
        self.nombreEntry.place(x=140,y=120,width=140,height=30)

        self.passwordEntry=tk.Entry(root)
        self.passwordEntry["borderwidth"] = "1px"
        # passwordEntry["font"] = ft
        self.passwordEntry["fg"] = "#333333"
        self.passwordEntry["justify"] = "left"
        self.passwordEntry["text"] = "Password_entry"
        self.passwordEntry["relief"] = "sunken"
        self.passwordEntry.place(x=140,y=80,width=141,height=30)

        usuarioLabel=tk.Label(root)
        # usuarioLabel["font"] = ft
        usuarioLabel["fg"] = "#333333"
        usuarioLabel["justify"] = "center"
        usuarioLabel["text"] = "Usuario"
        usuarioLabel.place(x=50,y=40,width=70,height=25)

        self.usuarioEntry=tk.Entry(root)
        self.usuarioEntry["borderwidth"] = "1px"
        # usuarioEntry["font"] = ft
        self.usuarioEntry["fg"] = "#333333"
        self.usuarioEntry["justify"] = "left"
        self.usuarioEntry["text"] = "Usuario_entry"
        self.usuarioEntry["relief"] = "sunken"
        self.usuarioEntry.place(x=140,y=40,width=141,height=30)

        telefonoLabel=tk.Label(root)
        telefonoLabel["anchor"] = "n"
        # telefonoLabel["font"] = ft
        telefonoLabel["fg"] = "#333333"
        telefonoLabel["justify"] = "center"
        telefonoLabel["text"] = "Telefono"
        telefonoLabel.place(x=50,y=240,width=70,height=25)

        telefonoEntry=tk.Entry(root)
        telefonoEntry["borderwidth"] = "1px"
        # telefonoEntry["font"] = ft
        telefonoEntry["fg"] = "#333333"
        telefonoEntry["justify"] = "left"
        telefonoEntry["text"] = "Telefono_entry"
        telefonoEntry["relief"] = "sunken"
        telefonoEntry.place(x=140,y=240,width=140,height=30)

        apellidoLabel=tk.Label(root)
        # apellidoLabel["font"] = ft
        apellidoLabel["fg"] = "#333333"
        apellidoLabel["justify"] = "center"
        apellidoLabel["text"] = "Apellido"
        apellidoLabel.place(x=50,y=160,width=70,height=25)


    def crearBotton_command(self):
        logica.botoncrear()
        print("command")


    def eliminarBotton_command(self):
        logica.botoneliminar()
        print("command")


    def consultarBotton_command(self):
        logica.botonconsultar()
        print("command")


    def modificarBotton_command(self):
        logica.botonmodificar()
        print("command")


class ingress(): #no esta funcionando
     def __init__(self, root):
        #setting title
        root.title("Integrador UTN")
        #setting window size
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)

        dniLabel=tk.Label(root)
        # dniLabel["font"] = ft
        dniLabel["fg"] = "#333333"
        dniLabel["justify"] = "center"
        dniLabel["text"] = "DNI"
        dniLabel.place(x=50,y=200,width=70,height=25)

        contultarBotton=tk.Button(root)
        contultarBotton["bg"] = "#fafafa"
        # contultarBotton["font"] = ft
        contultarBotton["fg"] = "#3d3d3d"
        contultarBotton["justify"] = "center"
        contultarBotton["text"] = "Consultar"
        contultarBotton.place(x=250,y=300,width=70,height=25)
        contultarBotton["command"] = self.consultarBotton_command

        eliminarBotton=tk.Button(root)
        eliminarBotton["bg"] = "#fafafa"
        # eliminarBotton["font"] = ft
        eliminarBotton["fg"] = "#3d3d3d"
        eliminarBotton["justify"] = "center"
        eliminarBotton["text"] = "Eliminar"
        eliminarBotton.place(x=170,y=300,width=70,height=25)
        eliminarBotton["command"] = self.eliminarBotton_command

        apellidoEntry=tk.Entry(root)
        apellidoEntry["borderwidth"] = "1px"
        # apellidoEntry["font"] = ft
        apellidoEntry["fg"] = "#333333"
        apellidoEntry["justify"] = "left"
        apellidoEntry["text"] = "Apellido_entry"
        apellidoEntry["relief"] = "sunken"
        apellidoEntry.place(x=140,y=160,width=141,height=30)

        dniEntry=tk.Entry(root)
        dniEntry["borderwidth"] = "1px"
        # dniEntry["font"] = ft
        dniEntry["fg"] = "#333333"
        dniEntry["justify"] = "left"
        dniEntry["text"] = "Dni_entry"
        dniEntry["relief"] = "sunken"
        dniEntry.place(x=140,y=200,width=142,height=30)

        modificarBotton=tk.Button(root)
        modificarBotton["bg"] = "#fafafa"
        # modificarBotton["font"] = ft
        modificarBotton["fg"] = "#3d3d3d"
        modificarBotton["justify"] = "center"
        modificarBotton["text"] = "Modificar"
        modificarBotton.place(x=90,y=300,width=70,height=25)
        modificarBotton["command"] = self.modificarBotton_command

        nombreLabel=tk.Label(root)
        # nombreLabel["font"] = ft
        nombreLabel["fg"] = "#333333"
        nombreLabel["justify"] = "center"
        nombreLabel["text"] = "Nombre"
        nombreLabel.place(x=50,y=120,width=70,height=25)

        passwordLabel=tk.Label(root)
        # passwordLabel["font"] = ft
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Password"
        passwordLabel.place(x=50,y=80,width=70,height=25)

        nombreEntry=tk.Entry(root)
        nombreEntry["borderwidth"] = "1px"
        # nombreEntry["font"] = ft
        nombreEntry["fg"] = "#333333"
        nombreEntry["justify"] = "left"
        nombreEntry["text"] = "Nombre_entry"
        nombreEntry["relief"] = "sunken"
        nombreEntry.place(x=140,y=120,width=140,height=30)

        passwordEntry=tk.Entry(root)
        passwordEntry["borderwidth"] = "1px"
        # passwordEntry["font"] = ft
        passwordEntry["fg"] = "#333333"
        passwordEntry["justify"] = "left"
        passwordEntry["text"] = "Password_entry"
        passwordEntry["relief"] = "sunken"
        passwordEntry.place(x=140,y=80,width=141,height=30)

        usuarioLabel=tk.Label(root)
        # usuarioLabel["font"] = ft
        usuarioLabel["fg"] = "#333333"
        usuarioLabel["justify"] = "center"
        usuarioLabel["text"] = "Usuario"
        usuarioLabel.place(x=50,y=40,width=70,height=25)

        usuarioEntry=tk.Entry(root)
        usuarioEntry["borderwidth"] = "1px"
        # usuarioEntry["font"] = ft
        usuarioEntry["fg"] = "#333333"
        usuarioEntry["justify"] = "left"
        usuarioEntry["text"] = "Usuario_entry"
        usuarioEntry["relief"] = "sunken"
        usuarioEntry.place(x=140,y=40,width=141,height=30)

        telefonoLabel=tk.Label(root)
        telefonoLabel["anchor"] = "n"
        # telefonoLabel["font"] = ft
        telefonoLabel["fg"] = "#333333"
        telefonoLabel["justify"] = "center"
        telefonoLabel["text"] = "Telefono"
        telefonoLabel.place(x=50,y=240,width=70,height=25)

        telefonoEntry=tk.Entry(root)
        telefonoEntry["borderwidth"] = "1px"
        # telefonoEntry["font"] = ft
        telefonoEntry["fg"] = "#333333"
        telefonoEntry["justify"] = "left"
        telefonoEntry["text"] = "Telefono_entry"
        telefonoEntry["relief"] = "sunken"
        telefonoEntry.place(x=140,y=240,width=140,height=30)

        apellidoLabel=tk.Label(root)
        # apellidoLabel["font"] = ft
        apellidoLabel["fg"] = "#333333"
        apellidoLabel["justify"] = "center"
        apellidoLabel["text"] = "Apellido"
        apellidoLabel.place(x=50,y=160,width=70,height=25)



if __name__ == "__main__":
    rootlogin = tk.Tk()
    app = loginApp(rootlogin)
    rootlogin.mainloop()
