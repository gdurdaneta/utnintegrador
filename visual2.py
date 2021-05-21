import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from modelobd import OperacionDB

class App:
    def __init__(self, root):
        #setting title
        root.title("Integrado!")
        
        #setting window size
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        GLabel_481=tk.Label(root)
        GLabel_481["fg"] = "#333333"
        GLabel_481["justify"] = "center"
        GLabel_481["text"] = "label"
        GLabel_481.place(x=160,y=460,width=171,height=30)

        self.botonconsulta=tk.Button(root)
        self.botonconsulta["bg"] = "#fafafa"
        self.botonconsulta["fg"] = "#3d3d3d"
        self.botonconsulta["justify"] = "center"
        self.botonconsulta["text"] = "Consultar"
        self.botonconsulta.place(x=230,y=160,width=70,height=25)
        self.botonconsulta["command"] = self.bconsulta

        self.botonelimina=tk.Button(root)
        self.botonelimina["bg"] = "#fafafa"
        self.botonelimina["fg"] = "#3d3d3d"
        self.botonelimina["justify"] = "center"
        self.botonelimina["text"] = "Eliminar"
        self.botonelimina.place(x=230,y=130,width=70,height=25)
        self.botonelimina["command"] = self.belimina

        self.botonmodifica=tk.Button(root)
        self.botonmodifica["bg"] = "#fafafa"
        self.botonmodifica["fg"] = "#3d3d3d"
        self.botonmodifica["justify"] = "center"
        self.botonmodifica["text"] = "Modificar"
        self.botonmodifica.place(x=230,y=100,width=70,height=25)
        self.botonmodifica["command"] = self.bmodifica

        self.validaEntry=tk.Entry(root)
        self.validaEntry["borderwidth"] = "1px"
        self.validaEntry["fg"] = "#333333"
        self.validaEntry["justify"] = "left"
        self.validaEntry["text"] = "Valida_entry"
        self.validaEntry["relief"] = "sunken"
        self.validaEntry.place(x=90,y=200,width=141,height=30)

        self.dataEntry=tk.Entry(root)
        self.dataEntry["borderwidth"] = "1px"
        self.dataEntry["fg"] = "#333333"
        self.dataEntry["justify"] = "left"
        self.dataEntry["text"] = "data_entry"
        self.dataEntry["relief"] = "sunken"
        self.dataEntry.place(x=90,y=60,width=141,height=30)

        self.cbPassword=tk.Checkbutton(root)
        self.cbPassword["fg"] = "#333333"
        self.cbPassword["justify"] = "center"
        self.cbPassword["text"] = "Password"
        self.cbPassword.place(x=30,y=100,width=70,height=25)
        self.cbPassword["offvalue"] = "0"
        self.cbPassword["onvalue"] = "1"
        self.cbPassword["command"] = self.bcbpassword

        self.cbNombre=tk.Checkbutton(root)
        self.cbNombre["fg"] = "#333333"
        self.cbNombre["justify"] = "center"
        self.cbNombre["text"] = "nombre"
        self.cbNombre.place(x=30,y=130,width=70,height=25)
        self.cbNombre["offvalue"] = "0"
        self.cbNombre["onvalue"] = "1"
        self.cbNombre["command"] = self.bcbnombre

        self.cbApellido=tk.Checkbutton(root)
        self.cbApellido["fg"] = "#333333"
        self.cbApellido["justify"] = "center"
        self.cbApellido["text"] = "Apellido"
        self.cbApellido.place(x=30,y=160,width=70,height=25)
        self.cbApellido["offvalue"] = "0"
        self.cbApellido["onvalue"] = "1"
        self.cbApellido["command"] = self.bcbapellido

        self.cbTelefono=tk.Checkbutton(root)
        self.cbTelefono["fg"] = "#333333"
        self.cbTelefono["justify"] = "center"
        self.cbTelefono["text"] = "Telefono"
        self.cbTelefono.place(x=150,y=100,width=70,height=25)
        self.cbTelefono["offvalue"] = "0"
        self.cbTelefono["onvalue"] = "1"
        self.cbTelefono["command"] = self.bcbtelefono

        self.cbDNI=tk.Checkbutton(root)
        self.cbDNI["fg"] = "#333333"
        self.cbDNI["justify"] = "center"
        self.cbDNI["text"] = "DNI"
        self.cbDNI.place(x=150,y=130,width=70,height=25)
        self.cbDNI["offvalue"] = "0"
        self.cbDNI["onvalue"] = "1"
        self.cbDNI["command"] = self.bcbdni

        #self.usuario = usuario

    def bconsulta(self):
        print(self.usuario)
        consulta = OperacionDB().consultageneral(self.usuarioEntry.get())
        messagebox.showinfo(message=consulta, title="Consulta")
        print(consulta)


    def belimina(self):
        OperacionDB().borrar(self.usuarioEntry.get(), self.passwordEntry.get())

    def bcbpassword(self):
        OperacionDB().modificarusuario("Password",self.dataEntry.get(), self.validaEntry.get())
      


    def bcbnombre(self):
        print("command")


    def bcbapellido(self):
        print("command")


    def bcbtelefono(self):
        print("command")


    def bcbdni(self):
        print("command")

    def bmodifica(self):
        print("command")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
